from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Role(models.Model):
	role_name = models.CharField(max_length=30)

	def __str__(self):
		return self.role_name

class Address(models.Model):
	city = models.TextField()
	street = models.TextField()
	neighborhood = models.TextField()
	gate_no = models.IntegerField()

class Category(models.Model):
	category_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.category_name

class Brand(models.Model):
	brand_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.brand_name

class Product(models.Model):
	BOOL_CHOICES = ((True, 'SATILDI'), (False, 'SATILMADI'))
	product_name = models.CharField(max_length = 50)
	product_price =models.DecimalField(max_digits=6, decimal_places=2)
	product_picture = models.ImageField(upload_to='static/images/',null = True, blank = True)
	product_status = models.BooleanField(default=False)
	product_brand = models.ForeignKey(Brand, on_delete =models.PROTECT)
	product_category = models.ForeignKey(Category, on_delete = models.PROTECT)

	def __str__(self):
		return self.product_name

class Basket(models.Model):
	product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
	basket_addition_date =models.DateTimeField(null = True, blank=True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, default = 1, related_name = 'Profile')
	name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	e_mail = models.CharField(max_length= 50)
	phone_number = models.CharField(max_length=11)
	birthdate = models.DateField(null=True, blank=True)
	BOOL_CHOICES = ((True, 'Male'), (False, 'Female'))
	gender = models.NullBooleanField(choices=BOOL_CHOICES, blank=True, null=True)
	address_id = models.ForeignKey(Address, on_delete = models.CASCADE,blank=True, null=True)
	basket_id = models.OneToOneField(Basket, on_delete = models.CASCADE,blank=True, null=True)
	
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)

class Product_processing(models.Model):
	user_purchaser_id = models.OneToOneField(User, on_delete = models.CASCADE, related_name='alici_id' )
	user_vendor_id = models.OneToOneField(User, on_delete = models.CASCADE,  related_name='satici_id')
	product_id = models.ForeignKey(Product, on_delete = models.CASCADE, default=0)

class Product_addition_log(models.Model):
	user_vendor_id = models.ForeignKey(User, on_delete = models.CASCADE)
	product_addition = models.DateTimeField(default=timezone.now)
	explanation= models.TextField()

class Product_sell_log(models.Model):
	user_purchaser_id = models.ForeignKey(User, on_delete = models.CASCADE)
	product_sell_date = models.DateTimeField(default=timezone.now)
	explanation = models.TextField()

