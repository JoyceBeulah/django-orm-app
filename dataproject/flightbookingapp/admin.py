from django.contrib import admin
from .models import Flightbooking, FlightbookingAdmin

admin.site.register(Flightbooking, FlightbookingAdmin)
