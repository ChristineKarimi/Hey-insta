from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile

# Create your tests here.

class PostTestClass(TestCase):

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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
testing the delete method

'''

    def test_delete_method(self):

        self.new_post.save_image()

        images = post.objects.all()

        self.new_post.delete_image()

        self.assertTrue(len(images)==0)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
'''
testing the update method for the image caption

'''

   def test_update_method(self):

        self.new_post.save_post()

        self.new_post.update_caption(self.new_image.id,'great day')

        image = post.objects.filter(caption='great day').all()

        self.assertTrue(len(post)==1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
  getting a post by id test

'''  
    
     def test_get_post_by_id(self):

        find_post = self.new_post.get_post_by_id(self.new_post.id)

        post = Post.objects.filter(id = self.new_post.id)

        self.assertTrue(find_post,post)

    def tearDown(self):

        Post.objects.all().delete()   