import os
import subprocess
class SystemControls:
    def __init__(self):
        self.hostname = subprocess.check_output(['hostname'])

    def getHostname(self):
        return self.hostname

    def reboot(self):
        os.system('reboot')

