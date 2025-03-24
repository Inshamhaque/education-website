# from django.test import TestCase
# from web.crypto import encrypt, decrypt
# from web.models import Profile
# from django.contrib.auth.models import User

# class EncryptionTests(TestCase):
#     def setUp(self):
#         self.test_user = User.objects.create_user(
#             username="testuser",
#             email="test@example.com",
#             password="testpassword"
#         )

#     def test_encryption_decryption(self):
#         """Test that our encryption and decryption functions work properly"""
#         original_text = "This is sensitive information"
#         encrypted = encrypt(original_text)
#         decrypted = decrypt(encrypted)

#         # The encrypted text should be different from the original
#         self.assertNotEqual(original_text, encrypted)
#         # Decryption should restore the original text
#         self.assertEqual(original_text, decrypted)

#     def test_encrypted_model_fields(self):
#         """Test that our encrypted fields work properly in models"""
#         sensitive_bio = "This is sensitive bio information"

#         # Create profile with sensitive info
#         profile = Profile.objects.get(user=self.test_user)
#         profile.bio = sensitive_bio
#         profile.save()

#         # Get a fresh instance from the database
#         db_profile = Profile.objects.get(id=profile.id)

#         # The retrieved bio should match the original
#         self.assertEqual(db_profile.bio, sensitive_bio)

#         # But the raw value in the database should be encrypted
#         # For this test, we'd need to access the raw DB value, which depends on your setup

#     # def test_key_rotation(self):
#     #     """Test behavior during key rotation scenarios"""
#     #     from web.crypto import encrypt, decrypt
#     #     from cryptography.fernet import Fernet
#     #     import mock

#     #     # Create and save an encrypted value
#     #     original_text = "This data was encrypted with the old key"
#     #     profile = Profile.objects.get(user=self.test_user)
#     #     profile.bio = original_text
#     #     profile.save()

#     #     # Simulate key rotation by temporarily changing the key
#     #     original_key = settings.ENCRYPTION_KEY
#     #     new_key = Fernet.generate_key()

#     #     # Note: In a real implementation, you'd need a more sophisticated
#     #     # key rotation mechanism that can handle both old and new keys

#     #     # Patch the settings to use the new key and test
#     #     with mock.patch('web.crypto.settings.ENCRYPTION_KEY', new_key):
#     #         # Attempting to decrypt old data with new key should raise an error
#     #         # or have a graceful fallback mechanism
#     #         rotated_profile = Profile.objects.get(id=profile.id)

#     #         # This will depend on your implementation's approach to handling
#     #         # decryption with the wrong key - either exception or fallback value
#     #         # self.assertNotEqual(rotated_profile.bio, original_text)
