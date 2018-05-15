from django.test import TestCase
from .models import Profile, Image


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    tests for the Profile model
    '''

    def setUp(self):
        # Setup fot test instances
        self.profile = Profile(profile_photo='me', bio='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    def test_save_profile(self):
        # test the save method for saving profiles
        self.profile.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles) > 0)

    def test_delete_profile(self):
        # test whether the function to delete profiles, removes profiles
        self.profile.save_profile()
        my_profile = Profile(profile_photo='NicholasCage.png', bio='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        my_profile.save_profile()
        self.profile.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles) == 1)


class ImageTestClass(TestCase):
    '''
    tests for the Image model
    '''

    def setUp(self):
        self.image = Image(image='NicholasCageWasHere', image_name='ThisAintAGame', image_caption='Cheezy, McAbdul',)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        my_image = Image.objects.get(image='NicholasCageWasHere', image_name='ThisAintAGame', image_caption='Cheezy, McAbdul')
        my_image.save_image()
        self.image.delete_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) == 0)
