from django.db import models
from django.utils.timezone import now

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="Unspecified")
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="market/images")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    address1 = models.CharField(max_length=500, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip = models.CharField(max_length=50, default="")
    itemsJson = models.CharField(max_length=2000, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status = models.CharField(max_length=500, default="order Placed")
    timestamp = models.DateField(auto_now_add=True, blank=True)
