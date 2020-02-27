from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .permissions import IsSellerOrReadOnly
from products.models import Product, ProductCategory
from products.api.serializers import ProductCategorySerializer, ProductSerializer, ProductSubcategorySerializer


class ProductListCreateView(APIView, PageNumberPagination):
    page_size = 8
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, request):
        order = self.request.query_params.get("orderby", default="id")
        subcategory = self.request.query_params.get("subcategory")
        if subcategory:
            products = Product.objects.filter(product_subcategory__name=subcategory.capitalize()).order_by(order)
        else:
            products = Product.objects.all().order_by(order)
        return self.paginate_queryset(products, self.request)

    def get(self, request):
        products = self.get_queryset(request=request)
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        self.check_object_permissions(self.request, request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsSellerOrReadOnly]

    def get_object(self, pk):
        product = get_object_or_404(Product, pk=pk)
        self.check_object_permissions(self.request, product)
        return product

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryListView(APIView):

    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
