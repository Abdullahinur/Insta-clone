from django.test import TestCase
from .models import Profile


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    class that test the characteristics of the Profile model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.profile = Profile(profile_photo='test_profile_photo', bio='test_bio')
