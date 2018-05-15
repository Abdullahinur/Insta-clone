from django.test import TestCase
from .models import Profile


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.abdullahinur = Profile(user='Abdullahinur', profile_photo='me', bio='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    # Testing instance of a USER
    def test_instance(self):
        self.assertTrue(isinstance(self.abdullahinur, Profile))
