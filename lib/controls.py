__author__ = "Oliver Rogers"
__version__ = "1.0.0"
__maintainer__ = "Oliver Rogers"
__email__ = "oliver.rogers101@gmail.com"
__status__ = "Development"
import os
import logging
import psutil
import subprocess
import socket

class SystemControls:
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.hostname = socket.gethostname() 

    def getHostname(self):
        self.logger.debug('Returning hostname value: {}'.format(self.hostname))
        return self.hostname

    def checkProcess(self,process_name):
        self.logger.debug('Running checkProcess function for {}'.format(process_name))
        command = 'ps -ef | grep {}'.format(process_name)
        ps_out = subprocess.Popen(command,
                                  shell=True,
                                  stdout=subprocess.PIPE)
        stout, _ = ps_out.communicate()
        print(stout)
 
    def getServiceDetails(self,service):
        key_value = subprocess.check_output(["systemctl", "show", service], universal_newlines=True).split('\n')
        json_dict = {}
        for entry in key_value:
            kv = entry.split("=", 1)
            if len(kv) == 2:
                json_dict[kv[0]] = kv[1]
        return json_dict


    def reboot(self):
        self.logger.debug('Running reboot command')
        os.system('reboot')


#sc = SystemControls('media-server-api')
#sc.find_procs_by_name('deluge')
#print(sc)
