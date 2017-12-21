import unittest
from app import app
import app as application

class Test_CalcOverall(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def test_CalcFunc(self):
        self.assertFalse(application.CalcOverall(0,0))

    def test_CalcFunc_returns_50(self):
        self.assertEqual(application.CalcOverall([100], [50]), '50.0')

    def test_CalcFunc_returns_75(self):
        self.assertEqual(application.CalcOverall([50, 50], [50, 100]), '75.0')


class FlaskEndpointsTest(unittest.TestCase): 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 


if __name__ == '__main__':
    unittest.main()
