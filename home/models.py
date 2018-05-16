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
    # Image class properties
    image = models.ImageField(upload_to="images/", null=True)
    image_name = models.CharField(max_length=30, null=True)
    image_caption = models.TextField(null=True)
    profile_key = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.PositiveIntegerField(default=0)
    comments_number = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        # Function to order most recent using pub date
        ordering = ['-pub_date']

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        retrived_image = Image.objects.get(id=id)
        return retrived_image

    @classmethod
    def get_images_by_user(cls,id):
        posted_images = Image.objects.filter(user_id=id)
        return posted_images

    @classmethod
    def get_all_images(cls):
        all_posted_images = cls.objects.all()
        return all_posted_images


    @classmethod
    def get_timeline_posts(cls):
        # Function to retrieve posts that the current user has
        timeline_posts = Image.objects.filter()


class Comment(models.Model):
    # properties for comments
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        # A method that saves the comment to the images
        self.save()

    def delete_comment(self):
        # A method to delete comments
        self.delete()

        
class Like(models.Model):
    pass
