from django.db import models
from django.contrib import admin
class Car(models.Model):
    reg_no=models.CharField(max_length=20,help_text="Car ID")
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    year=models.IntegerField()
class CarAdmin(admin.ModelAdmin):
    list_display=('reg_no','name','price','year')
