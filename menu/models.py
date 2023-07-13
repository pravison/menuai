from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class BestServedAt(models.Model):
    name = models.CharField(max_length=30, help_text='lunch , dinner...')

    class Meta:
        verbose_name_plural = 'Best served at'

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='media/img')
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True )
    ingredients = models.CharField(max_length=200, null=True, blank=True)
    overview = models.TextField(max_length=200, blank=True, null=True)
    description= models.TextField(max_length=500, blank=True, null=True)
    best_for = models.ManyToManyField(BestServedAt, blank=True )
    promotion = models.BooleanField(default=False, blank=True, null=True)
    special = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL , null= True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True )
    served = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems =self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems =self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL , null= True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL , null= True, blank=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return self.menu.name
        except:
            return f'no menu name'
    
    @property
    def get_total(self):
        try:
            total = self.menu.price * self.quantity
        except:
            total=0

        return total
    
class TableInfo(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL , null= True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL , null= True, blank=True)
    table_number = models.IntegerField(null= True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'table number {self.table_number}'



