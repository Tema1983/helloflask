import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from application import views
from tests import unittest

class helloTestCase(unittest.TestCase):
    def setUp(self):
        views.app.config['TESTING'] = True
        self.app = views.app.test_client()

    def tearDown(self):
        self.app = None

    def test_root(self):
        result = self.app.get('/')
        assert 'Hello World!' in result.data

    def test_user(self):
        result = self.app.get('/user/david')
        assert 'User david' in result.data

    def test_post_id_with_integer_success(self):
        result = self.app.get('/post_id/23')
        assert 'Post 23' in result.data

    def test_post_id_with_str_failure(self):
        result = self.app.get('/post_id/asd')
        assert '404 Not Found' in result.data        

    def test_post_success(self):
        result = self.app.post('/post')
        assert 'POST' in result.data

    def test_post_failure(self):
        result = self.app.get('/post')
        assert '405 Method Not Allowed' in result.data

    def test_cmd_get_failure(self):
        result = self.app.get('/command/git')
        assert '405 Method Not Allowed' in result.data

    def test_cmd_post_test(self):
        result = self.app.post('/command/git')
        assert 'test' in result.data

    def runTest():
        pass

if __name__ == '__main__':
    unittest.main()