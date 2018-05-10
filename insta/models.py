from django.db import models

# Create your models here.
class Profile(models.Model):
  bio = models.TextField(max_length = 30, blank = True)
  website = models.CharField(max_length=30, blank =True)
  phone_number = models.IntegerField(blank =True, null = True)
  location = models.CharField(max_length = 30, blank =True)
  birth_date = models.DateField(null =True, blank = True)

class Post(models.Model):
  title = models.CharField(max_length = 100)
  image = models.ImageField(upload_to = 'posts/')
  posted_on = models.DateTimeField(auto_now_add=True)
