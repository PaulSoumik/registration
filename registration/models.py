from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django import forms
# Create your models here.



class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='UserProfileInfo')
	Institute = models.CharField(max_length=200,blank=True)
	Department = models.CharField(max_length=200,blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfileInfo.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile, sender=User)




