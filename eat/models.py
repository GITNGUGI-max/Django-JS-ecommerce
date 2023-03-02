from django.db import models
from django.contrib.auth.models import User




class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):

        return self.name

class MenuItems(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(blank=True, null=True)

    class Meta:

        verbose_name_plural = "Menu Items"
    def __str__(self):

        return self.name
    
    @property
    def imageURL(self):

        try:
            url = self.image.url
        except:
            url=''
        return url
    
class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(MenuItems, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "Order Items"

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total
    
    def __str__(self):

        return str(self.id)

class ShippingAddress(models.Model):

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):

        return f'{self.address} - {self.date_added}' 