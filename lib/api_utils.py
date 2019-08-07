__author__ = "Oliver Rogers"
__version__ = "1.0.0"
__maintainer__ = "Oliver Rogers"
__email__ = "oliver.rogers101@gmail.com"
__status__ = "Development"

import logging
import json

class APIUtils:
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)

    def sendSuccess(self,
                    data=None):
        self.logger.debug('Entered sendSuccess function command')
        
        options = {
            type(None): {},
            type('string'): {'text': data},
            type({}): {'data': data}
        }

        self.logger.debug('Determining data response type of {}'.format(data))       
        data_dict = options[type(data)]
        self.logger.debug('Data response type selected as {}: {}'.format(type(data), data_dict))
        
        self.logger.debug('Forming success response with data: {}'.format(data_dict))
        base_res = {'status': 'success'}}

        res = {**base_res, **data_dict}
        self.logger.debug('Response formed: {}'.format(data_dict))
        
        return (json.dumps(res), 200) 
