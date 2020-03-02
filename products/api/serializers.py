from rest_framework import serializers

from products.models import ProductSubcategory, ProductCategory, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
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
