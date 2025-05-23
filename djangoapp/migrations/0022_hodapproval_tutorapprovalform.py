# Generated by Django 5.1.7 on 2025-04-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0021_application_form_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoDapproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentname', models.CharField(max_length=255)),
                ('admission_no', models.CharField(max_length=255)),
                ('university_no', models.CharField(max_length=255)),
                ('Branch', models.CharField(choices=[('Select', 'Select'), ('EEE', 'Electrical & Electronics'), ('ME', 'Mechanical'), ('CSE', 'Computer Science'), ('CE', 'Civil Engineering '), ('EC', 'Electroncs')], default='Select', max_length=6)),
                ('Subject', models.CharField(max_length=500)),
                ('Details', models.CharField(max_length=1500)),
                ('Semester', models.CharField(choices=[('0', 'Select'), ('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'), ('8', 'S8')], default='Select', max_length=10)),
                ('Tutor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tutorapprovalform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentname', models.CharField(max_length=255)),
                ('admission_no', models.CharField(max_length=255)),
                ('university_no', models.CharField(max_length=255)),
                ('Branch', models.CharField(choices=[('Select', 'Select'), ('EEE', 'Electrical & Electronics'), ('ME', 'Mechanical'), ('CSE', 'Computer Science'), ('CE', 'Civil Engineering '), ('EC', 'Electroncs')], default='Select', max_length=6)),
                ('Subject', models.CharField(max_length=500)),
                ('Details', models.CharField(max_length=1500)),
                ('Semester', models.CharField(choices=[('0', 'Select'), ('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'), ('8', 'S8')], default='Select', max_length=10)),
            ],
        ),
    ]
