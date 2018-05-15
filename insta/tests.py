from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile

# Create your tests here.

class PostTestClass(TestCase):

    def setUp(self):

        self.user = User.objects.create_user('kim','chris')

        self.post = Post.objects.create(image_link='posts/1.png',
                                              name ='flower',
                                              caption='beauty of life',
                                              created_by=self.user)

    def test_instance(self):

        self.image.save()

        self.assertTrue(isinstance(self.Post,Post))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
'''
saving a post functionality test

'''

    def test_save_method(self):

        self.new_Post.save_image()

        images = Post.objects.all()

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
'''
saving a profile picture test

'''

# class ProfileTestClass(TestCase):

#     def setUp(self):

#         self.profile=Profile(profile_photo='posts/me.jpg',Bio ='am awesome')

#         self.profile.save()

class ProfileTestClass(TestCase):

    def setUp(self):

        self.profile=Profile(profile_photo='pics/image1.jpg',
                                      Bio ='full stack dev')

        self.profile.save()

    def test_instance(self):

        self.assertTrue(isinstance(self.profile,Profile))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
save method test
'''
def test_save_method(self):

        self.profile.save_profile()

        profile = Profile.objects.all()

        self.assertTrue(len(profile)>0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

def test_delete_method(self):

        self.profile.save_profile()

        profile = Profile.objects.all()

        self.profile.delete_profile()

        self.assertTrue(len(profile)==0)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
'''
update profile test

'''
def test_update_method(self):

        new_profile = 'pics/7.png','code more'

        self.profile.update_profile(self.profile.id,new_profile)

        new_profile = Profile.objects.filter(profile_photo='pics/7.png',
                                                       Bio='code more and more')

        self.assertTrue(len(new_profile)==1)       

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class CommentTestClass(TestCase):
   """
   test case fo the comments
   
   """

# class CommentTestClass(TestCase):

#     def setUp(self):

#         self.comment=Comment(profile_photo='pics/image1.jpg',Bio ='full stack dev')

#         self.comment.save()

#     def test_instance(self):

#         self.assertTrue(isinstance(self.comment,Comment))        



   def setUp(self):
       self.new_user = User.objects.create_user("testuser", "chris")

       self.new_profile_t = Profile(profile_pic='profiles/profile1.jpg',
                                    profile_bio="full stack dev based in nairobi",
                                    profile_owner=self.new_user)
       self.new_profile_t.save()

       self.new_image = Image(image='photos/1.jpeg', image_name='kim',
                              image_caption="test image1", image_created_by=self.new_profile_t)
       self.new_image.save()

       self.new_comm = Comment(
           comment_image=self.new_image, comment_owner=self.new_profile_t, comment_post="test comment")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
           