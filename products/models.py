from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
# Create your models here.
class ProductModel(models.Model):
    # Return policy field
    RETURN_POLICY_CHOICES = [
        ('7D', '7 Days Return'),
        ('15D', '15 Days Return'),
        ('30D', '30 Days Return'),
        ('NR', 'No Return'),
    ]
    Product_name=models.CharField(max_length=400,blank=False,null=False)
    price=models.PositiveBigIntegerField()
    category=models.ForeignKey('category.CategoryModel',on_delete=models.CASCADE)
    stock_quantity=models.PositiveBigIntegerField()
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    brand=models.CharField(max_length=400,blank=False,null=False)
    image=models.ImageField(upload_to='Productimg')
    weight=models.CharField(max_length=200,null=True,blank=True)
    discount = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)],help_text='Please choose from 0–100%')
    rating=models.DecimalField(max_digits=2,decimal_places=1,default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    size=models.CharField(max_length=200,null=True,blank=True)
    warrenty_period=models.CharField(max_length=200,null=True,blank=True)
    retrun_policy=models.CharField(max_length=200,choices=RETURN_POLICY_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Product_name
    


    def save(self,*args,**kwargs):
        if self.discount:
            self.price-=(self.discount*self.price)//100
        return super().save(*args,**kwargs)




    

