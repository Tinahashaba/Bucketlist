import unittest
from app import app
from app.application import Application
from app.modal import User
from app.modal import Bucket


class TestApplicationRoutes(unittest.TestCase):
    """
    This class contains tests for the application routes.
    """

    def setUp(self):
        """
        This method activates the flask testing config flag, which disables
        error catching during request handling.
        The testing client always provided an interface to the application.
        :return:
        """
        app.testing = True
        self.app = app.test_client()
        self.application = Application()
        app.secret_key = "jfhjeeurhfjfieoosjdjdkiosooalaks0wssjsjk"

    def test_home_status_code(self):
        response = self.app.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_home_page_status_code(self):
        response = self.app.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_sign_up_page_status_code(self):
        response = self.app.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_404_page(self):
        response = self.app.get('/tinah', follow_redirects=True)
        self.assertIn(b'Page Not Found', response.data)

