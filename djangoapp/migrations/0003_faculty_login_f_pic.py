# Generated by Django 5.1.7 on 2025-03-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_login',
            name='f_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
