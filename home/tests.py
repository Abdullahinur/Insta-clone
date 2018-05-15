from django.test import TestCase
from .models import Profile


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    class that test the characteristics of the Profile model
    '''

    def setUp(self):
        # Setup fot test instances
        self.profile = Profile(profile_photo='me', bio='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    def test_save_profile(self):
        # test the save method for saving profiles
        self.profile.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles) > 0)
