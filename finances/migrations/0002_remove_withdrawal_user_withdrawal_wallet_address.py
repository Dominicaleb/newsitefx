# Generated by Django 4.1.6 on 2024-03-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawal',
            name='user',
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='wallet_address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]