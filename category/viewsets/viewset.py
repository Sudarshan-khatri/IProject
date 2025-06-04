from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import CategoryModel
from ..serializers.serializer import (
     ListCategorySerializer,
     RetrieveCategorySerializer,
     WriteCategorySerializer)


class CategoryViewset(viewsets.ModelViewSet):
    queryset=CategoryModel.objects.all().order_by('-id')
    permission_classes=[AllowAny]
    serializer_class=ListCategorySerializer


    
    def get_serializer_class(self):
        if self.action =='retrieve':
            return RetrieveCategorySerializer
        elif self.action in ['create','update','partial_update']:
            return WriteCategorySerializer
        return super().get_serializer_class()
    

    # def create(self, request, *args, **kwargs):
    #     is_many = isinstance(request.data, list)
    #     serializer = self.get_serializer(data=request.data, many=is_many)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    # def create(self, request, *args, **kwargs):
    #     if isinstance(request.data,list):
    #         serializer=self.get_serializer(data=request.data,many=True)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)  
    #     return super().create(request, *args, **kwargs)
    