from django.db import models


    
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


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    country = models.CharField(max_length=100, blank=True, null=True)

    # Add more custom fields easily:
    # phone = models.CharField(max_length=15, blank=True, null=True)
    # address = models.TextField(blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.email

