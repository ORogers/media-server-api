import os
import logging
import psutil
import subprocess

class SystemControls:
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.hostname = subprocess.check_output(['hostname'])

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
 
    def find_procs_by_name(self,name):
        "Return a list of processes matching 'name'."
        assert name, name
        ls = []
        for p in psutil.process_iter():
            name_, exe, cmdline = "", "", []
            try:
                name_ = p.name()
                cmdline = p.cmdline()
                exe = p.exe()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except psutil.NoSuchProcess:
                continue
            if name == name_ or cmdline[0] == name or os.path.basename(exe) == name:
                ls.append(name)
        return ls
    def reboot(self):
        self.logger.debug('Running reboot command')
        os.system('reboot')


#sc = SystemControls('media-server-api')
#sc.find_procs_by_name('deluge')
#print(sc)
