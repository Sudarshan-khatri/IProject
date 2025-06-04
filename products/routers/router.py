from rest_framework.routers import DefaultRouter
from  products.viewsets.viewset import ProductViewset



product_router=DefaultRouter()
product_router.register('Product',ProductViewset)