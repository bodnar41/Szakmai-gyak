from django.db import models

# Create your models here.

category_choice = (
		('Laptop', 'Laptop'),
		('IT Equipment', 'IT Equipment'),
	)


class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name


class Device(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
	device_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	manuf = models.CharField(max_length=50, blank=True, null=True)
	type = models.CharField(max_length=50, blank=True, null=True)
	serial_id = models.CharField(max_length=50, blank=True, null=True)
	guarantee = models.DateTimeField(auto_now_add=False, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.device_name + ' ' + str(self.serial_id) + ' ' + str(self.guarantee)