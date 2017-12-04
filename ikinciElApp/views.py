from django.shortcuts import  render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from ikinciElApp.models import *
from ikinciElApp.forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response



def home(request):
	return render(request,'home.html')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			)
			user.save()
			return redirect('home')
	else:
			form = SignupForm()      
	return render(request , 'signup.html',{'form': form})

@login_required
def user_profile(request):
	#user_id = request.user.id # giriş yapan user 'ın idsini alıyoruz.
	if not Profile.objects.filter(user=request.user.id):
		Profile.objects.create(user=request.user)
	if request.method == 'POST':
		address_form = forms.AddressForm(request.POST)
		if address_form.is_valid():
			address = address_form.save()
			form = UserProfile(request.POST,request.FILES,instance=request.user.Profile)
			if form.is_valid():
				form.save()
				# profile = Profile.create(
				# name = form.cleaned_data['name'],
				# last_name = form.cleaned_data['last_name'],
				# e_mail = form.cleaned_data['e_mail'],
				# phone_number = form.cleaned_data['phone_number'],
				# gender = form.cleaned_data['gender'],
				# birthdate = form.cleaned_data['birthdate'],
				# 	)
				# address = Address.objects.create(
				# 	city= form.cleaned_data['city'],
				# 	street= form.cleaned_data['street'],
				# 	neighborhood = form.cleaned_data['neighborhood'],
				# 	gate_no = form.cleaned_data['gate_no'],
				# 	)
				# profile.save()
				# address.save()
				return HttpResponseRedirect('/home/')

			else:
				form = UserProfile(instance=request.user.Profile)
	form = UserProfile()
	return render(request,'profile.html',{'form': form})

@login_required
def AddProduct(request):
	if request.method == 'POST':
		form = AddProductForm(request.POST,request.FILES)
		if form.is_valid():
			cat=Category.objects.get(id=form.cleaned_data['product_category'])
			brand = Brand.objects.get(id=form.cleaned_data['product_brand'])
			product = Product.objects.create(
			product_name=form.cleaned_data['product_name'],
			product_price=form.cleaned_data['product_price'],
			product_pictures=form.cleaned_data['product_pictures'],
			product_category=cat,
			product_brand =brand,
			)
			product.save()
			return HttpResponseRedirect('home')
	else:
		form = AddProductForm()
		return render(request,'AddProduct.html', {'form': form})

