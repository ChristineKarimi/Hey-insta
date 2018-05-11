from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile

# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):

        self.user =User.objects.create_user('misskim','ckk')

        self.image = Image.objects.create(image_link='posts/image1.png',name ='flower',caption='beauty of life',created_by=self.user)

    def test_instance(self):

        self.image.save()

        self.assertTrue(isinstance(self.Post,Post))
