# my example:
# from django.contrib.auth.models import User
# from .managers import PersonManager
#
# class Person(User):
#     objects = PersonManager()
#
#     class Meta:
#         proxy = True
#         ordering = ('first_name', )
#
#     def do_something(self):
#         ...
from django.db import models
from django.contrib.auth.models import User
# For Signals
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    bio = models.TextField(max_length=500, blank=True)














# # Define signals so Profile model will be automatically created and updated when user instances are created/updated
# # Hook methods to User Model whenever save event occurs
# @receiver(post_save, send=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
