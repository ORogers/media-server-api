__author__ = "Oliver Rogers"
__version__ = "1.0.0"
__maintainer__ = "Oliver Rogers"
__email__ = "oliver.rogers101@gmail.com"
__status__ = "Development"
import os
import logging
import subprocess
import socket

class SystemControls:
    def __init__(self,
                 logger,
                 services):
        self.logger = logging.getLogger(logger)
        self.hostname = socket.gethostname() 
        self.services = services



    def getHostname(self):
        try:
            self.logger.debug('Returning hostname value: {}'.format(self.hostname))
            return self.hostname
        except Exception as e:
            message = 'Error reading hostname: {}'
            self.logger.debug(message)
            raise Exception(message)    

    def getServiceDetails(self,service):
        self.logger.debug('Running getServiceDetails function')
        
        try:
            self.logger.debug('Attempting to read service details dict for {}'.format(service))
            key_value = subprocess.check_output(["systemctl", "show", service], universal_newlines=True).split('\n')
            
            json_dict = {}
            for entry in key_value:
                kv = entry.split("=", 1)
                if len(kv) == 2:
                    json_dict[kv[0]] = kv[1]

            self.logger.debug('full service data: {}'.format(json_dict))
            if json_dict.get('UnitFilePreset') == None:
                raise Exception("Service '{}' not found".format(service))
    
        except Exception as e:
            self.logger.debug('Error finding service details: {}'.format(e))
            raise Exception(e)

        try:
            self.logger.debug('Forming output dict')
            service_data = {
                'name': json_dict['Names'].replace('.service',''),
                'description': json_dict['Description'],
                'active': json_dict['ActiveState'] == 'active'  
            }
            self.logger.debug('Response dict: {}'.format(service_data))
        except Exception as e:
            message = 'Error forming response json: {}'.format(e)
            self.logger.error(message)
            raise Exception(e)

        return service_data

    def checkValidService(self,service):
            if service in self.services:
                return True
            else:

                raise Exception('Invalid Service: {} is not in the list of valid services'.format(service))

    def stopService(self,service):
        try:
            self.logger.debug('Running stopService function for service "{}"'.format(service))
            subprocess.check_call(['service',service,'stop'])
            return True
        except Exception as e:
            self.logger.error('Error stopping service: {}'.format(e))         

    def startService(self,service):
        try:
            self.logger.debug('Running stopService function for service "{}"'.format(service))
            subprocess.check_call(['service',service,'stop'])
            return True
        except Exception as e:
            self.logger.error('Error stopping service: {}'.format(e))
        
    def restartService(self,service):
        try:
            self.logger.debug('Running stopService function for service "{}"'.format(service))
            subprocess.check_call(['service',service,'stop'])
            return True
        except Exception as e:
            self.logger.error('Error stopping service: {}'.format(e))

    def reboot(self):
        self.logger.debug('Running reboot command')
        os.system('reboot')

    def getServices(self):
        self.logger.debug('Running getServices function')
        self.logger.debug('Returning service list: {}'.format(self.services))
        return self.services

