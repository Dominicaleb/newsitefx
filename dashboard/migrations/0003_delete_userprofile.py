# Generated by Django 4.1.6 on 2024-03-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userprofile_rename_creation_date_loan_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
