# Generated by Django 4.1.6 on 2024-03-13 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0002_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptodeposit',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='cryptodeposit',
            name='currency',
        ),
    ]