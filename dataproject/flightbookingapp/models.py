from django.db import models
from django.contrib import admin
class Flightbooking(models.Model):
    Cust_ID = models.IntegerField(primary_key=True)
    Cust_Name = models.CharField(max_length=100)
    Cust_Age = models.IntegerField()
    Cust_Email = models.EmailField()
    Cust_Gender = models.CharField(max_length=100)

class FlightbookingAdmin(admin.ModelAdmin):
    list_display = ('Cust_ID','Cust_Name','Cust_Age','Cust_Email','Cust_Gender')