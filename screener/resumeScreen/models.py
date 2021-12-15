from django.db import models

class UploadResume(models.Model):
    name = models.CharField(max_length=30)
    #job_des_skills = models.CharField(max_length=100)
    #job_des_degree = models.CharField(max_length=100)
    job_des = models.FileField(upload_to='job_description',blank=True,null=True)
    job_resume = models.FileField(upload_to='job_resume',blank=True,null=True)
    job_des_skills = models.CharField(max_length=100,blank=True,null=True)
    job_des_degree = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.names
    

