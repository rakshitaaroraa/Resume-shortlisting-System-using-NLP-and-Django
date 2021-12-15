# Generated by Django 2.2.3 on 2019-07-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('job_des', models.FileField(blank=True, null=True, upload_to='job_description')),
                ('job_resume', models.FileField(blank=True, null=True, upload_to='job_resume')),
            ],
        ),
    ]
