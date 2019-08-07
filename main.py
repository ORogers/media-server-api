from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from controls import SystemControls
import os
import logging

'''Setup Logging'''
logger_name = 'media-server-api'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m %H:%M',
                    filename='./{}.log'.format(logger_name),
                    filemode='w')

logger = logging.getLogger(logger_name)

app = Flask(__name__)
system = SystemControls(logger=logger_name)


@app.route('/')
def index():
    hostname = system.getHostname()
    return('This API controls the media server running on {}.'.format(hostname))


@app.route('/hostname')
def hostname():
    return system.getHostname()

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



### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


if  __name__ == '__main__':
    app.run(host='0.0.0.0')
