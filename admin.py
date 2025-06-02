from django.contrib import admin
from .models import BrightFurnitureUser, FurnitureData

# Register your models here.



class AdminBrightFurnitureUser(admin.ModelAdmin):
    list_display=['id','created_at','name','email','phone','message']
admin.site.register(BrightFurnitureUser, AdminBrightFurnitureUser)

class AdminFurnitureData(admin.ModelAdmin):
    list_display = ['id', 'furniture_name', 'furniture_price', 'furniture_category']
admin.site.register(FurnitureData, AdminFurnitureData)
