# web/migrations/0044_encrypt_pii_fields.py
from django.db import migrations

from web.fields import EncryptedCharField, EncryptedEmailField, EncryptedTextField


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0043_alter_studygroup_members_studygroupinvite"),  # This is the latest migration
    ]

    operations = [
        # Profile Model
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=EncryptedTextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="expertise",
            field=EncryptedCharField(max_length=200, blank=True),
        ),
        # WebRequest Model
        migrations.AlterField(
            model_name="webrequest",
            name="ip_address",
            field=EncryptedCharField(max_length=100, blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="webrequest",
            name="user",
            field=EncryptedCharField(max_length=150, blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="webrequest",
            name="agent",
            field=EncryptedTextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="webrequest",
            name="referer",
            field=EncryptedCharField(max_length=255, blank=True, default=""),
        ),
        # Order Model
        migrations.AlterField(
            model_name="order",
            name="tracking_number",
            field=EncryptedCharField(max_length=100, blank=True),
        ),
        # Donation Model
        migrations.AlterField(
            model_name="donation",
            name="email",
            field=EncryptedEmailField(),
        ),
        migrations.AlterField(
            model_name="donation",
            name="stripe_payment_intent_id",
            field=EncryptedCharField(max_length=100, blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="donation",
            name="stripe_subscription_id",
            field=EncryptedCharField(max_length=100, blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="donation",
            name="stripe_customer_id",
            field=EncryptedCharField(max_length=100, blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="donation",
            name="message",
            field=EncryptedTextField(blank=True),
        ),
        # Additional donation fields
        migrations.AlterField(
            model_name="donation",
            name="donor_name",
            field=EncryptedCharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="donation",
            name="donor_email",
            field=EncryptedEmailField(max_length=254, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="donation",
            name="donor_address",
            field=EncryptedTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="donation",
            name="donor_phone",
            field=EncryptedCharField(max_length=50, blank=True, null=True),
        ),
    ]
