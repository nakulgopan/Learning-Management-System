# Generated by Django 5.1.7 on 2025-03-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_alter_faculty_login_f_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_login',
            name='f_branch',
            field=models.CharField(choices=[('Select', 'Select'), ('EEE', 'Electrical & Electronics'), ('ME', 'Mechanical'), ('CSE', 'Computer Science'), ('CE', 'Civil Engineering '), ('EC', 'Electroncs')], default='Select', max_length=6),
        ),
        migrations.AlterField(
            model_name='student_login',
            name='s_branch',
            field=models.CharField(choices=[('Select', 'Select'), ('EEE', 'Electrical & Electronics'), ('ME', 'Mechanical'), ('CSE', 'Computer Science'), ('CE', 'Civil Engineering '), ('EC', 'Electroncs')], default='Select', max_length=6),
        ),
    ]
