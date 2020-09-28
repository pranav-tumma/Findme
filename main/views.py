from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Police, Compliant
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
	user = request.user
	# # citizen = Citizen.objects.first()
	# fname = user.name.split(" ")[0]
	# length = user.citizen.compliant_set.filter(status='Pending').count() + user.citizen.appointment_set.filter(status='Pending').count() + user.citizen.noc_set.filter(status='Pending').count()
	# context = {"home_page" : "active", 'user' : user, 'length' : length, 'fname':fname}
	context = {}
	return render(request, 'Findme/mainpage.html', context)

def vehicle_status(request):
	if request.method == "POST":
		veh_id = request.POST.get('veh_id')
		try:
			compliant = Compliant.objects.get(vehicle_id=str(veh_id))
		except Compliant.DoesNotExist:
			compliant=None
		if not compliant:
			return render(request, 'Findme/vechilestatus.html')
		else:
			status = compliant.status
			context = {'status' : status}
			return render(request, 'Findme/vechilestatus.html', context)
	else:
		context = {}
		return render(request, 'Findme/vechilestatus.html', context)


def compliant(request):
	if request.method == "POST":
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		address = request.POST.get('Address')
		veh_no = request.POST.get('Vechile.No')
		model = request.POST.get('Model/Registration Details')
		
		compliant = Compliant(
		    vehicle_id = veh_no,
		    fullname=name,
		    mobile = phone,
		    email = email,
		    address = address,
		    model = model
		)

		compliant.save()
	context = {}
	return render(request, 'Findme/complaintregister.html', context)

def loginView(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_staff:
			login(request, user)
			return redirect('dashboard')
		else:
			return redirect('login')
	context = {}
	return render(request, 'Findme/login page.html', context)

def logoutView(request):
	logout(request)
	return redirect('login')


def register(request):
	if request.method == "POST":
		username = request.POST.get('Username')
		name = request.POST.get('name')
		f, l = name.split(" ")
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		state = request.POST.get('state')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if(password2 != password1):
			return render(request, 'Findme/registerpage.html')
		new_user = User.objects.create_user(
		    username, email, password1, 
		    first_name=f,
		    last_name=l,
		)

		new_user.save()

		police = Police(
		    police=new_user,
		    name=name,
		    phone=phone
		)
		police.save()
	context = {}

	return render(request, 'Findme/registerpage.html', context)
	