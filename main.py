__author__ = "Oliver Rogers"
__version__ = "0.0.1"
__maintainer__ = "Oliver Rogers"
__email__ = "oliver.rogers101@gmail.com"
__status__ = "Development"


#System Imports
import os
import sys
sys.path.insert(0,'./lib')
import json
import logging

#Library Imports
from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from controls import SystemControls

'''
___  ___         _ _              _____                                  ___  ______ _____ 
|  \/  |        | (_)            /  ___|                                / _ \ | ___ \_   _|
| .  . | ___  __| |_  __ _ ______\ `--.  ___ _ ____   _____ _ __ ______/ /_\ \| |_/ / | |  
| |\/| |/ _ \/ _` | |/ _` |______|`--. \/ _ \ '__\ \ / / _ \ '__|______|  _  ||  __/  | |  
| |  | |  __/ (_| | | (_| |      /\__/ /  __/ |   \ V /  __/ |         | | | || |    _| |_ 
\_|  |_/\___|\__,_|_|\__,_|      \____/ \___|_|    \_/ \___|_|         \_| |_/\_|    \___/ 
'''
  
#Setup Logging
logger_name = 'media-server-api'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m %H:%M',
                    filename='./{}.log'.format(logger_name),
                    filemode='w')

logger = logging.getLogger(logger_name)
#Finished Logging setup

#Initialize objects
app = Flask(__name__)
system = SystemControls(logger=logger_name)

#API routes
@app.route('/')
def index():
    hostname = system.getHostname()
    return 'This API controls the media server running on {}.'.format(hostname)


@app.route('/hostname')
def hostname():
    try:
        logger.debug('Calling getHostname function')
        hostname = system.getHostname()
        logger.debug('Hostname recieved: {}'.format(hostname))
        
        logger.debug('forming re')

        res = {
            'status': 'success',
            'response': {
                'hostname': hostname
            }
        }

        return (json.dumps(res), 200)

    except Exception as e:
        logger.error('Error during /hostname request: {}'.format(e))
        return (_ , 500)
        

@app.route('/process')
def getProcess():
    try:
        logger.debug('Parsing url argument for process name')
        process_name = request.args.get('p')
        logger.debug('Value {} has been parsed for the value of "p"'.format(process_name))
        if process_name ==  None:
            raise Exception('No value of "p" passed in HTTP request.') 
    except Exception as e:
        logger.debug('Error finding process details: {}'.format(e))
        return 'Error finding process details: {}'.format(e) 


    return process_name


@app.route('/reboot')
@app.route('/restart')
def restart():
    try:
        system.reboot()
        return('Success')
    except Exception as e:
        return('Failed')


#Swagger Specific
swagger_url = '/swagger'
swagger_api_url = '/static/swagger.json'
logger.debug('Setting up Swagger with swagger.json at {}'.format(swagger_api_url))
swagger_blueprint = get_swaggerui_blueprint(
    swagger_url,
    swagger_api_url,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)
logger.debug('Swagger setup complete')
#End Swagger setup 


if  __name__ == '__main__':
    app.run(host='0.0.0.0')
