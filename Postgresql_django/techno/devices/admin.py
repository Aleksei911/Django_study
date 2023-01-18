from django.contrib import admin
from .models import Device, Device_model, Device_color, Device_manufacturer

# Register your models here.
admin.site.register(Device)
admin.site.register(Device_model)
admin.site.register(Device_color)
admin.site.register(Device_manufacturer)