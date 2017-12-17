from django.shortcuts import  render ,get_object_or_404
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
from django.views import generic
from django.utils import timezone
from reportlab.pdfgen import canvas
from io import BytesIO


def write_pdf_product(request,id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    product = Product.objects.get(id=id)
    product = str(product.product_name)+" - "+str(product.product_price)
    # product = str(product)
    p.drawString(100, 100, product)
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
def write_pdf_user(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    users = User.objects.all()
    users = str(users)
    # product = str(product)
    p.drawString(100, 100, users)
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


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
			return redirect('/login')
	else:
			form = SignupForm()      
	return render(request , 'signup.html',{'form': form})

@login_required
def user_profile(request):
	if request.method == 'GET':
		if not Profile.objects.filter(user=request.user.id):
			Profile.objects.create(user=request.user)
	if request.method == 'POST':
		form = AddProfileForm(request.POST,instance=request.user.profile)
		if form.is_valid():
			user = request.user
			address = Address.objects.create(
			city= form.cleaned_data['city'],
			street= form.cleaned_data['street'],
			neighborhood = form.cleaned_data['neighborhood'],
			gate_no = form.cleaned_data['gate_no'],
			)
			address.save()
			profile = Profile.objects.filter(user=request.user.id)
			profile.update(
			user = user,
			name = form.cleaned_data['name'],
			last_name = form.cleaned_data['last_name'],
			e_mail = form.cleaned_data['e_mail'],
			phone_number = form.cleaned_data['phone_number'],
			gender = form.cleaned_data['gender'],
			birthdate = form.cleaned_data['birthdate'],
			address_id = address,
			)
			return HttpResponseRedirect('/profile_list')
		else:
			form = AddProfileForm(instance=request.user.profile)
	form = AddProfileForm()
	return render(request,'profile.html',{'form': form})

def user_profile_list(request):
	profile = Profile.objects.filter(user=request.user.id)
	return render(request, 'profile_list.html', {'data': profile})

@login_required
def AddProduct(request):
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			cat=Category.objects.get(id=form.cleaned_data['product_category'])
			brand = Brand.objects.get(id=form.cleaned_data['product_brand'])
			product_seller = User.objects.get(id = request.user.id)
			product = Product.objects.create(
			product_name=form.cleaned_data['product_name'],
			product_price=form.cleaned_data['product_price'],
			#product_pictures=form.cleaned_data['product_pictures'],
			product_category=cat,
			product_brand =brand,
			product_seller = product_seller
			)
			product.save()
			now = timezone.now()
			pro_add =Product_addition_log.objects.create(user_seller=product_seller,product_addition=now,explanation='Ürün Eklendi.')
			pro_add.save()
			return HttpResponseRedirect('/product')
	else:
		form = AddProductForm()
		return render(request,'AddProduct.html', {'form': form})

def product_list(request):
	products = Product.objects.all()
	return render(request, 'product_list.html', {'data': products})

def addToBasket(request,id):
	product = Product.objects.get(id=id)
	now = timezone.now()
	buyer = User.objects.get(id = request.user.id)
	add_basket = Basket.objects.create(product_id = product,basket_addition_date = now,buyer_id = buyer)
	add_basket.save()
	profile = Profile.objects.filter(user = request.user.id)
	return HttpResponseRedirect('/product')

def basket_list(request):
	baskets = Basket.objects.filter(buyer_id = request.user.id)	
	return render(request, 'basket.html',{'data': baskets})

def buy_product(request,id):
	pro = Product.objects.filter(id = id)
	buyer_user = User.objects.get(id = request.user.id)
	# product_seller = Product.objects.filter('product_seller' = )
	# seller_user = Product.objects.get()
	# pro_process =Product_processing.objects.create(user_buyer= buyer_user , user_seller = seller_user, product_id = pro)
	# pro_process.save()
	now = timezone.now()
	pro_sell =Product_sell_log.objects.create(user_buyer=buyer_user,product_sell_date=now,explanation='Ürün Satıldı.')
	pro_sell.save()
	pro.delete()
	return HttpResponseRedirect('/product')

	




