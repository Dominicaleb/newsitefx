# Generated by Django 4.1.6 on 2024-03-14 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0004_rename_username_cryptodeposit_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptodeposit',
            old_name='currency',
            new_name='username',
        ),
    ]
