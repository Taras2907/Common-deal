from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination

from products.models import ProductSubcategory, ProductCategory, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    manufacturer = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductSubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSubcategory
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = "__all__"