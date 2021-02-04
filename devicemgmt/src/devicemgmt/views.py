from django.shortcuts import render, redirect
from .models import *
from .forms import DeviceCreateForm, DeviceSearchForm, DeviceUpdateForm


# Create your views here.

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,

    }
    return render(request, "home.html", context)


def list_devices(request):
    header = 'List of Devices'
    form = DeviceSearchForm(request.POST or None)
    queryset = Device.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Device.objects.filter(device_name__icontains=form['device_name'].value(),
                                        category__icontains=form['category'].value(),
                                        manuf__icontains=form['manuf'].value()
                                         )
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "list_devices.html", context)


def add_devices(request):
    form = DeviceCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_devices')
    context = {
        "form": form,
        "title": "Add Device",
    }
    return render(request, "add_devices.html", context)

def update_devices(request, pk):
	queryset = Device.objects.get(id=pk)
	form = DeviceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = DeviceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_devices')

	context = {
		'form':form
	}
	return render(request, 'add_devices.html', context)


def delete_devices(request, pk):
	queryset = Device.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_devices')
	return render(request, 'delete_devices.html')

