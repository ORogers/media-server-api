__author__ = "Oliver Rogers"
__version__ = "0.0.1"
__maintainer__ = "Oliver Rogers"
__email__ = "oliver.rogers101@gmail.com"
__status__ = "Development"

'''
___  ___         _ _              _____                                  ___  ______ _____ 
|  \/  |        | (_)            /  ___|                                / _ \ | ___ \_   _|
| .  . | ___  __| |_  __ _ ______\ `--.  ___ _ ____   _____ _ __ ______/ /_\ \| |_/ / | |  
| |\/| |/ _ \/ _` | |/ _` |______|`--. \/ _ \ '__\ \ / / _ \ '__|______|  _  ||  __/  | |  
| |  | |  __/ (_| | | (_| |      /\__/ /  __/ |   \ V /  __/ |         | | | || |    _| |_ 
\_|  |_/\___|\__,_|_|\__,_|      \____/ \___|_|    \_/ \___|_|         \_| |_/\_|    \___/ 
'''

#System Imports
import os
import logging
import sys
sys.path.insert(0,'./lib')

#Library Imports
from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from controls import SystemControls
from api_utils import APIUtils

#Setup Logging
logger_name = 'media-server-api'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m %H:%M',
                    filename='./{}.log'.format(logger_name),
                    filemode='w')

logger = logging.getLogger(logger_name)

#Initialize objects
app = Flask(__name__)
utils = APIUtils(logger=logger_name)

#Loading config
dir_path = os.path.dirname(os.path.realpath(__file__))
config = utils.loadConfig(dir_path+'/cfg/config.yml')

system = SystemControls(logger=logger_name,
                        services=config['services'])
#API routes
@app.route('/')
def index():
    try:
        hostname = system.getHostname()
        message = 'This API controls the media server running on {}.'.format(hostname)
        return utils.sendSuccess(message)
    except Exception as e:
        return utils.sendFailure(e)

@app.route('/hostname')
def hostname():
    try:
        logger.debug('Calling getHostname function')
        hostname = system.getHostname()
        logger.debug('Hostname recieved: {}'.format(hostname))
        
        data = {'hostname': hostname}
       
        return utils.sendFailure(data)

    except Exception as e:
        message = 'Error during /hostname request: {}'.format(e)
        logger.error(message)
        return utils.sendFailure(message)
        

@app.route('/service')
def getService():
    try:
        logger.debug('Parsing url argument for service name')
        service_name = request.args.get('name')
        logger.debug('Value {} has been parsed for the value of "name"'.format(service_name))
        if service_name ==  None:
            raise Exception('No value of "name" passed in HTTP request.') 
    except Exception as e:
        message = 'Error parsing url, missing "name" value: {}'.format(e)
        logger.debug(message)
        return utils.sendFailure(message)

    try:
        logger.debug('Calling function to retreive service data')
        service_data = system.getServiceDetails(service_name)
        logger.debug('Service data received: {}'.format(service_data))
    except Exception as e:
        message = 'Error retreiving service data: {}'.format(e)
        logger.debug(message)
        return utils.sendFailure(message)

    return utils.sendSuccess(service_data)


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
