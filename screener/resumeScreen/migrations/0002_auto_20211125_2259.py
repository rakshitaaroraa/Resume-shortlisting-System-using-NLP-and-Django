# Generated by Django 3.2.4 on 2021-11-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeScreen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadresume',
            name='job_des_degree',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadresume',
            name='job_des_skills',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
