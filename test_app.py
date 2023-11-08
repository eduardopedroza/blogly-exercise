from unittest import TestCase
from app import app, db
from models import User, Post


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

    def test_show_post_details(self):
        """Test showing the details of a post."""
        with self.client as c:
            response = c.get(f'/posts/{self.post_id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Test Post', response.data)

    def test_delete_post(self):
        """Test deleting a post."""
        with self.client as c:
            response = c.post(f'/posts/{self.post_id}/delete', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # Verify the post has been deleted
            post = Post.query.get(self.post_id)
            self.assertIsNone(post)
