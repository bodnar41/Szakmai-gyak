import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import *
from .forms import DeviceCreateForm, DeviceSearchForm, DeviceUpdateForm
from django.contrib import messages
import schedule
from datetime import datetime
import smtplib
from email.message import EmailMessage
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,

    }
    return render(request, "home.html", context)

@login_required
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
                                        manuf__icontains=form['manuf'].value(),
                                        serial_id__icontains=form['serial_id'].value(),
                                        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of devices.csv"'
            writer = csv.writer(response)
            writer.writerow(['DEVICE NAME', 'CATEGORY', 'QUANTITY', 'MANUFACTURER', 'TYPE', 'SERIAL ID', 'GUARANTEE'])
            instance = queryset
            for device in instance:
                writer.writerow([device.device_name, device.category, device.quantity, device.manuf, device.type, device.serial_id, device.guarantee])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "list_devices.html", context)

@login_required
def add_devices(request):
    form = DeviceCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully saved')
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
        messages.success(request, 'Successfully deleted')
        return redirect('/list_devices')
    return render(request, 'delete_devices.html')


def JobForm(t):
    queryset = Device.objects.all()

    currend_date = str(datetime.now())
    currend_date = datetime.strptime(currend_date, "%Y-%m-%d %H:%M:%S.%f")


    message_list = []
    sending_message = []

    for device in queryset:
        stored_date = device.guarantee

        stored_date = str(stored_date.isoformat("T", "milliseconds"))

        stored_date = datetime.strptime(stored_date, '%Y-%m-%dT%H:%M:%S.%f%z')


        if currend_date.year - stored_date.year == 0 and currend_date.month - stored_date.month < 2:
            message_list.append([device.device_name, device.serial_id, str(device.guarantee)])
        else:
            pass

    EMAIL_ADDRESS = "pythontesztweb@gmail.com"
    EMAIL_PASSWD = "Pythonteszt1"

    msg = EmailMessage()
    msg['Subject'] = 'Alert!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    for i in message_list:
        sending_message.append(f'Device name: {i[0]}, Serial ID: {i[1]} will expire on {i[2]}!')

    msg.set_content(str(sending_message))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWD)

        smtp.send_message(msg)
    print("Hello", t)
    return


# schedule.every().day.at("02:03").do(JobForm, 'Data check')
#
# while True:
#     schedule.run_pending()
#     time.sleep(60) # wait one minute

