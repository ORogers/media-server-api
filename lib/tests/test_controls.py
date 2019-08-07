import sys
sys.path.insert(0,'../')
import unittest
from controls import SystemControls

class TestController(unittest.TestCase):

    def setUp(self):
        self.system = SystemControls('test')

    def test_getHostname(self):
        try:
            self.system.getHostname()
            assert True
        except:
            assert False

    def test_checkProcess(self):
        try:
           self.system.checkProcess('deluge')
           assert True
        except:
           assert False

    def test_checkProcess01(self):
        try:
           self.system.checkProcess('deluge-web')
           assert True
        except:
           assert False

    def test_checkProcess02(self):
        try:
           self.system.checkProcess('Plex Media Server')
           assert True
        except:
           assert False


if __name__ == 'main':
    unittest.main()
