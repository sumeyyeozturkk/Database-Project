from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save,pre_delete,post_delete
from django.dispatch import receiver
import os
from django.db.models import Sum,Count
from django.db import connection  

class Role(models.Model):
	role_name = models.CharField(max_length=30)

	def __str__(self):
		return str(self.id)

class Address(models.Model):
	city = models.TextField()
	street = models.TextField()
	neighborhood = models.TextField()
	gate_no = models.IntegerField()

	def __str__(self):
		return str(self.id)


class Category(models.Model):
	category_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.category_name

class Brand(models.Model):
	brand_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.brand_name

def images_path(instance,file_name):
	uzanti = os.path.splitext(file_name)[-1]
	file_register_name = os.path.join('profile_images',str(instance.user.id)+uzanti)

class Product(models.Model):
	BOOL_CHOICES = ((True, 'SATILDI'), (False, 'SATILMADI'))
	product_name = models.CharField(max_length = 50)
	product_price =models.DecimalField(max_digits=6, decimal_places=2)
	#product_picture = models.ImageField(upload_to='static/images/',null = True, blank = True)
	product_brand = models.ForeignKey(Brand, on_delete =models.PROTECT)
	product_category = models.ForeignKey(Category, on_delete = models.PROTECT)
	product_seller = models.ForeignKey(User,on_delete= models.PROTECT,default = 1)

	def __str__(self):
		return str(self.id)

	@staticmethod  
	def search(search_string):  
		# create a cursor  
		cur = connection.cursor()  
		# execute the stored procedure passing in   
		# search_string as a parameter  
		cur.callproc('searcher_profileName_search', [search_string,])  
		# grab the results  
		results = cur.fetchall()  
		cur.close()  
		# wrap the results up into Product domain objects   
		return [Product(*row) for row in results]  
		
class Basket(models.Model):

	product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
	basket_addition_date =models.DateTimeField(null = True, blank=True)
	buyer_id = models.ForeignKey(User,on_delete=models.PROTECT)
	
	def __str__(self):
		return str(self.id)

	def BasketSumProduct():
		total = Basket.objects.filter('buyer_id').Count()
		return total

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name = 'profile')
	name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	e_mail = models.EmailField(max_length= 50)
	phone_number = models.CharField(max_length=11)
	profile_picture = models.ImageField('profile picture', upload_to='static/pictures/', null=True, blank=True)
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

@receiver(pre_delete, sender=User)
def delete_user_profile(sender,instance,**kwargs):
		Profile.objects.filter(user=instance).delete()

pre_delete.connect(delete_user_profile,sender=User)

# @receiver(pre_delete,sender=Profile)
# def delete_address(sender,instance,**kwargs):
# 	Address.objects.filter(address_id = instance.id).delete()
# pre_delete.connect(delete_address,sender=Profile)

class Product_processing(models.Model):
	user_buyer = models.OneToOneField(User, on_delete = models.CASCADE, related_name='alici_id' )
	user_seller = models.OneToOneField(User, on_delete = models.CASCADE,  related_name='satici_id')
	product_id = models.ForeignKey(Product, on_delete = models.CASCADE, default=0)

class Product_addition_log(models.Model):
	user_seller = models.ForeignKey(User, on_delete = models.CASCADE)
	product_addition = models.DateTimeField(default=timezone.now())
	explanation= models.TextField()


class Product_sell_log(models.Model):
	user_buyer = models.ForeignKey(User, on_delete = models.CASCADE)
	product_sell_date = models.DateTimeField(default=timezone.now())
	explanation = models.TextField()

