from unittest import TestCase
from app import app, db
from models import User

class UserViewsTests(TestCase):

    def test_user_detail_page(self):
        # Test the user detail page
        response = self.app.get(f'/users/{self.user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test User', response.data)

    def test_user_edit_page(self):
        # Test the user edit page GET request
        response = self.app.get(f'/users/{self.user_id}/edit')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Edit User', response.data)

    def test_user_delete(self):
        # Test deleting the user
        response = self.app.post(f'/users/{self.user_id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Check that the user is not in the database
        user = User.query.get(self.user_id)
        self.assertIsNone(user)
