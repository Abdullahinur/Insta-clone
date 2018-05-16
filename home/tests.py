from django.test import TestCase
from .models import Profile, Image, Comment, Like


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    tests for the Profile model
    '''

    def setUp(self):
        # Setup for test instances
        self.profile = Profile(profile_photo='me', bio='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    def test_instance(self):
        # test to check Profile instance
        self.assertTrue(isinstance(self.profile, Profile))

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

    def test_find_profile(self):
        # test whether search function works
        self.profile.save_profile()
        my_profile = Profile(profile_photo='NicholasCage.png', bio='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        my_profile.save_profile()
        search_profile = Profile.find_profile('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        self.assertTrue(len(search_profile) == 1)


class ImageTestClass(TestCase):
    '''
    tests for the Image Class
    '''

    def setUp(self):
        # Setup for test instances
        self.image = Image(image='NicholasCageWasHere', image_name='ThisAintAGame', image_caption='Cheezy, McAbdul',)

    def test_instance(self):
        # test to check Image instance
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        # test to save Image instance
        self.image.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) > 0)

    def test_delete_image(self):
        # test to delete Image instance
        self.image.save_image()
        my_image = Image.objects.get(image='NicholasCageWasHere', image_name='ThisAintAGame', image_caption='Cheezy, McAbdul')
        my_image.save_image()
        self.image.delete_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) == 0)

    def test_update_caption(self):
        # test the update caption function
        self.image.save_image()
        image = Image.objects.get(image='NicholasCageWasHere')
        image.update_caption('Cheezy McAbdul, with Fries and a Shake')
        image = Image.objects.get(image='NicholasCageWasHere')
        self.assertTrue(image.image_caption == 'Cheezy McAbdul, with Fries and a Shake')

class CommentTestClass(TestCase):
    '''
    test for the Comments class
    '''

    def setUp(self):
        # Setup for test instances
        self.my_comment = Comment(comment= "Oh no!!Not The Bees!!")
        self.new_comment.save()

    def test_instance(self):
        # test the instance of the my comment
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        # test whether comment can be saved
        self.my_comment.save_comment()
        all_comments = Comment.objects.all()
        self.assertTrue(len(all_comments) > 0)

    def test_delete_comment(self):
        # test whether comments can be deleted
        self.my_comment.save_comment()
        test_comment = Comment("What!? More Bees!?")
        test_comment.save_comment()
        self.new_comment.delete_comment()
        all_comments = Coment.objects.all()
        self.assertTrue(len(all_comments) == 1)


class LikeTestClass(TestCase):
    '''
    test for the Like class
    '''
    def setUp(self):
        # Setup for test instances
        self.new_like = Like(likes_number=0)

    def test_instance(self):
        # test the instance of the likes
        self.assertTrue(isinstance(self.new_like, Like))

    def test_save_likes(self):
        # test whether likes are saved
        self.new_like.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) > 0)

    def test_remove_like(self):
        self.new_like.save_like
        self.new_like.remove_like()
        like_status = self.new_like.likes_number
        self.assertTrue(like_status == 2)
