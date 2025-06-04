from rest_framework import serializers
from ..models import CategoryModel


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryModel
        fields='__all__'



class RetrieveCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryModel
        fields=['Category','slug','Description']



class WriteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryModel
        fields='__all__'