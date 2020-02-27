from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination

from products.models import ProductSubcategory, ProductCategory, Product


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()
    product_subcategory = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    subcategories = ProductSubcategorySerializer(many=True)

    class Meta:
        model = ProductCategory
        fields = "__all__"
