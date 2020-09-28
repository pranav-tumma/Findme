from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin

class Police(models.Model):
	police = models.ForeignKey(User, on_delete=models.CASCADE)
	# extra data
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=10, null=True)

	def __str__(self):
		return str(self.name)

class Compliant(models.Model):
	vehicle_id = models.CharField(max_length=50, unique=True)
	fullname = models.CharField(max_length=50)
	mobile = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	date_created = date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=50, default="Pending")

	
	def __str__(self):
		return str(self.fullname)






