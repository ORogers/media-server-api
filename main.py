from flask import Flask
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


if  __name__ == '__main__':
    app.run(host='0.0.0.0')
