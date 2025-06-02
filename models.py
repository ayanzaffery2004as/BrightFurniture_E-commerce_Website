from django.db import models

# Create your models here.
class BrightFurnitureUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True,null=True,blank=True)
    message = models.TextField(null=True,blank=True)


class FurnitureData(models.Model):
    furniture_img = models.URLField(max_length=200, null=True, blank=True)
    furniture_name = models.CharField(max_length=100)
    furniture_price = models.DecimalField(max_digits=10, decimal_places=2)
    furniture_description = models.TextField()
    furniture_category = models.CharField(max_length=50)
