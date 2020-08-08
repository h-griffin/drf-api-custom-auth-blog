from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Post.objects.create(
            title = 'title of post',
            author = test_user,
            description = 'Words about the post'
        )
        test_post.save()

    def test_tank_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(post.title, 'title of post')
        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.description, 'Words about the post')
