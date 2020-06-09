from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def home(request) :
	if request.user.is_authenticated :
		return redirect(reverse('home'))
	return render(request,'account/signup.html')
	

def signup(request) :

	if request.method=='POST' :
		if request.user.is_authenticated :
			logout(request)
		mail = request.POST.get('email','')
		username=request.POST.get('username','')
		password = request.POST.get('password','')
		confpassword = request.POST.get('confpassword','')

		check = User.objects.filter(username=username) | User.objects.filter(email = mail)

		if check :
			messages.error(request,'Username or email already exists')
			return redirect('/')

		if password==confpassword :
			user_obj = User.objects.create_user(password=password,email=mail,username=username)
			user_obj.save()

	return redirect('/')

def signin(request) :
	if request.method=='POST' :
		username = request.POST.get('username','')
		password = request.POST.get('password','')

		user = authenticate(username=username,password=password)

		if user is not None :
			login(request,user)
			messages.success(request,'Logged in')
			return redirect(reverse('home'))
		else :
			messages.error(request,'Invalid Ceredentials')
			return redirect("/")
	return render(request,'account/login.html')

def user_out(request) :
	logout(request)
	messages.success(request,"Successfully logged out")
	return redirect('/')
