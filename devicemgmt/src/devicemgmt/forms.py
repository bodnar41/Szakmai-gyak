from django import forms
from .models import Device

class DeviceCreateForm(forms.ModelForm):
   class Meta:
     model = Device
     fields = ['device_name', 'category', 'quantity', 'manuf', 'type', 'guarantee']

   def clean_type(self):
       type = self.cleaned_data.get('type')
       if not type:
           raise forms.ValidationError('This field is required')
       # for instance in Device.objects.all():
       #     if instance.category == type:
       #         raise forms.ValidationError(str(type) + ' is already created')
       return type

   def clean_guarantee(self):
       guarantee = self.cleaned_data.get('guarantee')
       if not guarantee:
           raise forms.ValidationError('This field is required')
       return guarantee


class DeviceSearchForm(forms.ModelForm):
   class Meta:
     model = Device
     fields = ['device_name', 'category', 'manuf']


class DeviceUpdateForm(forms.ModelForm):
	class Meta:
		model = Device
		fields = ['device_name', 'category', 'quantity', 'manuf', 'type', 'guarantee']