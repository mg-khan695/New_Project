from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product_add(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_name=models.CharField(default="Name", max_length=50)
    product_price=models.IntegerField(default="0")
    category=models.CharField(default="" ,max_length=50)
    product_image=models.ImageField(upload_to='media/')
    #first_name=models.CharField(default="First Name",max_length=50)
    # last_name=models.CharField(default="Last Name",max_length=50)
    # username=models.CharField(default="UserName",max_length=50)


