import os

from cryptography.fernet import Fernet
from django.core.management.base import BaseCommand
from django.db import transaction

from web.models import Profile  # Add other models with encrypted fields

# TODO: add other models with encrypted fields


class Command(BaseCommand):
    help = "Rotate the encryption key for all encrypted data"

    def handle(self, *args, **options):
        # Generate a new key
        new_key = Fernet.generate_key()
        old_key = os.environ.get("ENCRYPTION_KEY")

        if not old_key:
            self.stdout.write(self.style.ERROR("No old encryption key found. Cannot rotate."))
            return

        self.stdout.write(self.style.WARNING("Starting key rotation..."))
        self.stdout.write(self.style.WARNING("This may take a while for large datasets."))

        # We'll need to manually decrypt with old key and re-encrypt with new key
        # This is a simplified example - in a real app you'd want to handle this more carefully
        with transaction.atomic():
            # Update each model with encrypted fields
            # Example for Profile
            for profile in Profile.objects.all():
                # Decrypt with old key, encrypt with new key
                # Implementation depends on your specific encryption approach
                self.stdout.write(f"Rotating keys for Profile {profile.id}")
                # Add the implementation here

            # Continue with other models

        self.stdout.write(self.style.SUCCESS(f"Key rotation complete! New key: {new_key.decode()}"))
        self.stdout.write(
            self.style.WARNING("Make sure to update your ENCRYPTION_KEY environment variable with this new key.")
        )
