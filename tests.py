from flaskblog import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Kinetic Labs' in response.data)

    def test_aboutpage(self):
        tester = app.test_client(self)
        response = tester.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertTrue((b'About Page' in response.data))

if __name__ == "__main__":
    unittest.main()
