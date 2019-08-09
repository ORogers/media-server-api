import sys
import json
sys.path.insert(0,'../')
import unittest
from api_utils import APIUtils

class TestAPIUtils(unittest.TestCase):

    def setUp(self):
        self.utils = APIUtils('test')

    def test_sendSuccess(self):
        try:
            res =  self.utils.sendSuccess()
        except Exception as e:
            print(e)
            assert False
        assert True

    def test_sendSuccess01(self):
        try:
            data = {'test': 'data'}
            res =  self.utils.sendSuccess(data)
        except:
            assert False
        assert True

    def test_sendSuccess02(self):
        try:
            data = 'this is a unit test'
            res =  self.utils.sendSuccess(data)
        except:
            assert False
        assert True

    def test_sendFailure(self):
        try:
            res =  self.utils.sendFailure(None,404)
        except:
            assert False
        assert True

    def test_sendFailure01(self):
        try:
            data = {'test': 2}
            res =  self.utils.sendFailure(data)
        except:
            assert False
        assert True

    def test_sendFailure02(self):
        try:
            data = 'this is a unit test'
            res =  self.utils.sendFailure(data)
        except:
            assert False
        assert True
   

if __name__ == 'main':
    unittest.main()
