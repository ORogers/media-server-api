import sys
sys.path.insert(0,'../')
import unittest
from api_utils import APIUtils

class TestController(unittest.TestCase):

    def setUp(self):
        self.utils = APIUtils('test')

    def test_sendSuccess(self):
        try:
            res =  self.utils.sendSuccess()
        except:
            assert False
        target = {'status': 'success'}
        self.assertEqual(res, target)

    def test_sendSuccess01(self):
        try:
            data = {'test': 'data'}
            res =  self.utils.sendSuccess(data)
        except:
            assert False
        target = {'status': 'success', 'data': data}
        self.assertEqual(res, target)

if __name__ == 'main':
    unittest.main()
