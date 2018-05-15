from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile

# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):

        self.user =User.objects.create_user('misskim','ckk')

        self.post = Post.objects.create(image_link='posts/1.png',name ='flower',caption='beauty of life',created_by=self.user)

    def test_instance(self):

        self.image.save()

        self.assertTrue(isinstance(self.Post,Post))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
'''
saving post functionality test

'''

    def test_save_method(self):

        self.new_image.save_image()

        images = Image.objects.all()

        self.assertTrue(len(images)>0)        
