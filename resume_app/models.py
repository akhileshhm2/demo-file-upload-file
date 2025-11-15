from django.db import models

class Signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    country = models.CharField(max_length=100, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.email

    
# class ImgUpload(models.Model):
#     title=models.CharField(max_length=100)
#     photos=models.ImageField(upload_to='pictures/')

#     def __str__(self):
#         return self.title  
# 
from django.db import models

class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

