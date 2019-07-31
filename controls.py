import os
import subprocess

class SystemControls:
    def __init__(self):
        self.hostname = subprocess.check_output(['hostname'])

    def getHostname(self):
        return self.hostname

    def checkProcess(self,process_name):
        command = 'ps -ef | grep {}'.format(process_name)
        ps_out = subprocess.check_output(['ps', '-ef', '|', 'grep','hi'])
        print(ps_out)
 
    def reboot(self):
        os.system('reboot')


#sc = SystemControls()
#sc.checkProcess('deluge')
