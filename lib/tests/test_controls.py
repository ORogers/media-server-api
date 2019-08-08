import sys
sys.path.insert(0,'../')
import unittest
from controls import SystemControls

class TestController(unittest.TestCase):

    def setUp(self):
        self.system = SystemControls('test')
        self.service_keys = ['name', 'description', 'status']

    def test_getHostname(self):
        try:
            self.system.getHostname()
            assert True
        except:
            assert False

    def test_getServiceDetails(self):
        try:
           res = self.system.getServiceDetails('deluged')
           assert True 
        except:
           assert False

    def test_getServiceDetails01(self):
        try:
           self.system.getServiceDetails('deluge-web')
           assert True
        except:
           assert False

    def test_getServiceDetails02(self):
        try:
           self.system.getServiceDetails('plexmediaserver')
           assert True
        except:
           assert False

    def test_getServiceDetails03(self):
        #Should throw exception
        try:
           self.system.getServiceDetails('pleeex')
           assert False
        except:
           assert True

    def test_getServiceDetails04(self):
        #Should throw exception
        try:
           self.system.getServiceDetails('padegrareae././ws\leeex')
           assert False
        except:
           assert True


    def test_getServices(self):
        try:
            services = self.system.getServices()
            assert  True
        except:
            assert False

if __name__ == 'main':
    unittest.main()

