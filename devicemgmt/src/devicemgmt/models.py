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
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	device_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	manuf = models.CharField(max_length=50, blank=True, null=True)
	type= models.CharField(max_length=50, blank=False, null=True)
	guarantee = models.DateTimeField(blank=False, null=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.device_name + ' ' + str(self.quantity)