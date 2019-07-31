from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from controls import SystemControls

import os

app = Flask(__name__)
system = SystemControls()


@app.route('/')
def index():
    hostname = system.getHostname()
    return('This API controls the media server running on {}.'.format(hostname))


@app.route('/hostname')
def hostname():
    return system.getHostname()


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
