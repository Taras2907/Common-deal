from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView, ProductCategoryListView

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list"),

    path("products/<int:pk>/", ProductRetrieveUpdateDeleteView.as_view(), name="product-detail"),

    path("product-categories/", ProductCategoryListView.as_view(), name="product-categories-list")
]
