# Generated by Django 2.1 on 2020-01-06 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
