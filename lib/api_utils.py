__author__ = "Oliver Rogers"
__version__ = "1.0.0"
__maintainer__ = "Oliver Rogers"
__email__ = "oliver.rogers101@gmail.com"
__status__ = "Development"

import logging
import json
import yaml

class APIUtils:
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)

    def sendSuccess(self,
                    data=None,
                    status_code=200):
        self.logger.debug('Entered sendSuccess function')
        

        data_dict = self._selectPayloadType(data)
        base_res = {'status': 'success'}


        self.logger.debug('Forming success response with data: {}'.format(data_dict))
        res = {**base_res, **data_dict}
        self.logger.debug('Response formed: {}'.format(res))

        return (json.dumps(res), status_code) 

    def sendFailure(self,
                    data=None,
                    status_code=500):
        self.logger.debug('Entered sendFailure function')


        data_dict = self._selectPayloadType(data)
        base_res = {'status': 'failure'}


        self.logger.debug('Forming failure response with data: {}'.format(data_dict))
        res = {**base_res, **data_dict}
        self.logger.debug('Response formed: {}'.format(res))

        return (json.dumps(res), status_code) 

    def _selectPayloadType(self,data):
        self.logger.debug('Determining data response type of {}'.format(data))
        payloadType = {
            type(None): {},
            type('string'): {'message': data},
            type({}): {'data': data}
        }
        data_dict = payloadType[type(data)]
        self.logger.debug('Data response type selected as {}: {}'.format(type(data), data_dict))
        return data_dict

    def loadConfig(self,path):
        self.logger.debug('Running loadConfig function for {}'.format(path))
        with open(path, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as e:
                raise Exception(e)

        return config

