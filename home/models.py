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


# Create your models here.
# This is the Profile class where the Properties are defined
class Profile(models.Model):
    # user profiles properties
    username = models.CharField(max_length=30, default='User')
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True)
    bio = models.TextField(default="Awww, Shucks..it's a secret", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__():
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to="images/", null=True)
    image_name = models.CharField(max_length=30, null=True)
    image_caption = models.TextField(null=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
