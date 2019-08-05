import os
import subprocess

class SystemControls:
    def __init__(self):
        self.hostname = subprocess.check_output(['hostname'])

    def getHostname(self):
        return self.hostname

    def checkProcess(self,process_name):
        command = 'ps -ef | grep {}'.format(process_name)
        ps_out = subprocess.Popen(command,
                                  shell=True,
                                  stdout=subprocess.PIPE)
        stout, _ = ps_out.communicate()
        print(stout)
 
    def reboot(self):
        os.system('reboot')


sc = SystemControls()
sc.checkProcess('deluge')
