from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
        ('failed', 'Failed'),
        ('on_hold', 'On Hold'),
    ]

    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    shipping_address=models.TextField(null=False,blank=False)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    def save(self,*args,**kwargs):
        return super().save(*args, **kwargs)
    


class orderItem(models.Model):
    order=models.ForeignKey('orders.OrderModel',on_delete=models.CASCADE)
    product=models.ForeignKey('products.productModel',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def save(self,*args,**kwargs):
        self.price*=self.quantity
        return super().save(*args,**kwargs)