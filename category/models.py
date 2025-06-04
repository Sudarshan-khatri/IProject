from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
class CategoryModel(models.Model):
    Category=models.CharField(max_length=200,blank=False,null=False,unique=True)
    slug=models.SlugField(unique=True,blank=True)
    Description=models.TextField(max_length=3500,blank=True,null=True)
    

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Category


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.Category)
        super().save(*args,**kwargs)

