from django.test import TestCase
from core.models import Profile, Store, Request

class ProfileModelTest(TestCase):
    def setUp(self):
        # Create A test Profile Instance
        self.profile = Profile.objects.create(
            user_id=1,
            is_online=True
        )

    def test_profile_creation(self):
        """Test Profile Model Creation"""
        self.assertEqual(self.profile.user_id, 1)
        self.assertTrue(self.profile.is_online)

    def test_profile_str_representation(self):
                """Test the string representation of the Profile model."""
                self.assertEqual(str(self.profile), f"Profile of User {self.profile.user_id}")