import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['WTF_CSRF_ENABLED'] = False

    # helper methods
    def signup(self, username, password):
        return self.client.post(
            '/signup',
            data=dict(username=username, password=password),
            follow_redirects=True)

    def login(self, username, password):
        return self.client.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True)

    def logout(self):
        return self.client.post('/logout', follow_redirects=True)

    #Tests
    def Test_homepage(self):
        # test if homepage is returned
        response = self.client.get('/')
        self.assertEqual(response.status, '200 OK')

    def Test_signup_page(self):
        # test to check if signup page is live
        response = self.client.get('/signup')
        self.assertEqual(response.status, '200 OK')

    def Test_login_page(self):
        # test to check login page is live
        response = self.client.get('/login')
        self.assertEqual(response.status, '200 OK')

    def Test_signup(self):
        # test to check that signup works
        response = self.signup("lee", "12345")
        self.assertIn(b'Home', response.data)

    def Test_user_exists(self):
        # test to check that username is unique
        response = self.signup('lee', '12345')
        self.assertIn(b'Username already taken', response.data)

    def Test_login(self):
        # test to check that one can login
        self.signup('becky', 'laland')
        self.logout()
        response = self.login('becky', 'laland')
        self.assertIn(b'Home', response.data)

    def Test_Invalid_login(self):
        # test to check that one cannot login with invalid credentials
        self.signup('John', '13131')
        self.logout()
        response = self.login('John', '112233')
        self.assertIn(b'Invalid credentials', response.data)

    def Test_bucket_is_created_and_deleted(self):
        # test to check that a bucket is created and deleted when one is logged in
        self.signup('Jane', '14141')
        response = self.client.post(
            '/view/create_bucket',
            data=dict(bucket="Hiking"),
            follow_redirects=True)
        self.assertIn(b'Hiking', response.data)
        response = self.client.post(
            '/bucket/delete_bucket/0', follow_redirects=True)
        self.assertNotIn(b'Hiking', response.data)

    def Test_logout(self):
        # test to check that logout works
        self.signup('john', '12345')
        response = self.logout()
        self.assertIn(b'Bucket List', response.data)