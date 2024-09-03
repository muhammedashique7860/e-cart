from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def  __str__(self) -> str:
        return self.name
    
class Sub_category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,related_name='sub_categories', on_delete=models.CASCADE)
    
    def  __str__(self) -> str:
        return self.name


class Brand(models.Model):
     name=models.CharField(max_length=255)

     def __str__(self) -> str:
         return self.name

class Product(models.Model):
    Availability=(('In Stock','In Stock')),(('Out Of Stock','Out Of Stock'))


    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    Availability =models.CharField(choices=Availability,null=True,max_length=100)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name 
    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class Contact_us(models.Model):
    name=models.CharField(max_length=125)
    email=models.EmailField()
    subject=models.CharField(max_length=124)
    message=models.TextField()

    def __str__(self) -> str:
        return self.email 
    

class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.CharField(max_length=1000,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    quantity=models.IntegerField()
    total =models.CharField(max_length=100,default="")
    address=models.TextField()
    phone=models.BigIntegerField()
    pincode=models.BigIntegerField()
    
    date=models.DateField(default=datetime.datetime.today)
   





    def  __str__(self) -> str:
        return self.product



    