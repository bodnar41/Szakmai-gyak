from django import forms
from .models import Device

class DeviceCreateForm(forms.ModelForm):
   class Meta:
     model = Device
     fields = ['device_name', 'category', 'quantity', 'manuf', 'type', 'serial_id',  'guarantee']

   def clean_serial_id(self):
       serial_id = self.cleaned_data.get('serial_id')
       if not serial_id:
           raise forms.ValidationError('This field is required')

       return serial_id

   def clean_guarantee(self):
       guarantee = self.cleaned_data.get('guarantee')
       if not guarantee:
           raise forms.ValidationError('This field is required')
       return guarantee


class DeviceSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   class Meta:
     model = Device
     fields = ['device_name', 'manuf', 'serial_id']


class DeviceUpdateForm(forms.ModelForm):
	class Meta:
		model = Device
		fields = ['device_name', 'category', 'quantity', 'manuf', 'type', 'serial_id', 'guarantee']


