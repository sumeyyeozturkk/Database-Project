from django import forms
from .models import *
from django.contrib.auth.models import User
import re
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.forms.extras.widgets import SelectDateWidget


class SignupForm(forms.Form):

	username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30,placeholder='Username')), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False,placeholder='Choose a password')),min_length=6, label=_("Password"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False,placeholder='Confirm password')), label=_("Password (again)"))
	
	def clean_username(self):
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(_("The username already exists. Please try another one."))

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
		return self.cleaned_data

class AddProductForm(forms.Form):
	choices_category=Category.objects.all().values_list()
	choices_brand = Brand.objects.all().values_list()
	product_name=forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='Product Name')))
	#product_picture=forms.ImageField(widget=forms.TextInput(attrs=dict(required=True,placeholder='Product Name')))
	product_price=forms.RegexField(regex=r'^\d+(.\d{1,2})?$', widget=forms.TextInput(attrs=dict(required=True,placeholder='Price')))
	product_category=forms.ChoiceField(choices=choices_category, widget=forms.Select(attrs=dict(required=True,placeholder='Category')))
	product_brand = forms.ChoiceField(choices=choices_brand, widget=forms.Select(attrs=dict(required=True,placeholder='Brand')))

class AddProfileForm(forms.ModelForm):
	BOOL_CHOICES = ((True, 'Male'), (False, 'Female'))
	# name=forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='Name')))
	# last_name=forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='Last Name')))
	# e_mail = forms.EmailField(max_length=254,widget=forms.TextInput(attrs=dict(required=True,placeholder='e_mail')))
	# phone_number=forms.CharField(max_length =11 ,widget=forms.TextInput(attrs=dict(required=True,placeholder='Phone Number')))
	gender = forms.TypedChoiceField(choices=BOOL_CHOICES, widget=forms.RadioSelect(attrs=dict(required=True)),coerce=bool)
	birthdate = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=range(1995, 2017)))
	city = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='City')))
	street = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='Street')))
	neighborhood = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='neighborhood')))
	gate_no = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,placeholder='Gate No')))			

	class Meta:
		model = Profile
		fields = ('name','last_name','e_mail','phone_number','gender','birthdate','city','street','neighborhood','gate_no')



