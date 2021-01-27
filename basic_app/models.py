from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# user class already has name, email and password
# this class is to add extra attributes
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)

    # pillow library for images
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
