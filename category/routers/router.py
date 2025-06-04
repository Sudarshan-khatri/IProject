from rest_framework.routers import DefaultRouter
from category.viewsets.viewset import CategoryViewset

#create the url for category

category_router=DefaultRouter()
category_router.register('Category',CategoryViewset)