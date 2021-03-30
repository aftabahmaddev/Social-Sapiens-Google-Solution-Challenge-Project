from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class post(models.Model):
    varified= models.BooleanField(default=False) 
    solved= models.BooleanField(default=False) 
    img1=models.ImageField(null=True, blank=True,upload_to='img')
    img2=models.ImageField(null=True, blank=True,upload_to='img')
    img3=models.ImageField(null=True, blank=True,upload_to='img')
    img4=models.ImageField(null=True, blank=True,upload_to='img')
    img5=models.ImageField(null=True, blank=True,upload_to='img')
    video=models.FileField(null=True,blank=True,upload_to='video')
    name=models.CharField(max_length=100)
    des=models.TextField()
    about_payment=models.TextField()
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=15, null=True,blank=True)
    phone2=models.CharField(max_length=15, null=True,blank=True)
    province_types = (
        ('Punjab', 'Punjab'),
        ('Sindh', 'Sindh'),
        ('KP', 'KP'),
        ('Balochistan', 'Balochistan'),
        ('Islamabad', 'Islamabad'),
    )
    province=models.CharField(max_length=20, choices=province_types)
    city=models.CharField(max_length=45)
    address=models.TextField()
    def __str__(self):
        return self.name 
