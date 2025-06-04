from rest_framework import serializers
from  products.models import ProductModel


class ListProudctSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'



class RetrieveProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields=['Product_name','price','category',' owner','stock_quantity','brand','image','weight','discount','rating','size','warrenty_period','retrun_policy']



class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        mode=ProductModel
        fields=['Product_name','price','category',' owner','stock_quantity','brand','image','weight','discount','rating','size','warrenty_period','retrun_policy']

        