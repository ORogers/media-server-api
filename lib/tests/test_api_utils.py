import sys
import json
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
        target = (json.dumps({'status': 'success'}),200)
        self.assertEqual(res, target)

    def test_sendSuccess01(self):
        try:
            data = {'test': 'data'}
            res =  self.utils.sendSuccess(data)
        except:
            assert False
        target = (json.dumps({'status': 'success', 'data': data}),200)
        self.assertEqual(res, target)

if __name__ == 'main':
    unittest.main()
