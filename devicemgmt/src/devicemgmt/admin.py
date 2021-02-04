from django.contrib import admin
from .forms import DeviceCreateForm

# Register your models here.

from .models import Device

class DeviceCreateAdmin(admin.ModelAdmin):
   list_display = ['device_name', 'category', 'quantity', 'manuf', 'type', 'guarantee']
   form = DeviceCreateForm
   list_filter = ['category']
   search_fields = ['category', 'device_name', 'manuf', 'guarantee']

admin.site.register(Device, DeviceCreateAdmin)