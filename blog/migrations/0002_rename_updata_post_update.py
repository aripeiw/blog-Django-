# Generated by Django 4.0.6 on 2022-07-24 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updata',
            new_name='update',
        ),
    ]
