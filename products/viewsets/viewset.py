from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from products.serializers.serializer import ListProudctSerializer,RetrieveProductSerializers,WriteProductSerializer
from products.models import ProductModel


class ProductViewset(viewsets.ModelViewSet):
    queryset=ProductModel.objects.all().order_by('-id')
    permission_classes=[IsAuthenticated]
    serializer_class=ListProudctSerializer



    def get_serializer_class(self):
        if self.action =='retrieve':
            return RetrieveProductSerializers
        elif self.action in['create','update','partial_update']:
            return WriteProductSerializer
        return super().get_serializer_class()
    
        

    def get_queryset(self):
        user=self.request.user

        if user.is_anonymous:
            return ProductModel.objects.filter(stock_quantity__gt=0)
        if user.role=='admin':
            return ProductModel.object.all()
        elif user.role=='vendor':
            return ProductModel.objects.filter(owner=user)
        elif user.role=='customer':
             return ProductModel.objects.filter(stock_quantity__gt=0)
        return ProductModel.objects.none()
        
        

