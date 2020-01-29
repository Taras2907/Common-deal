from django.urls import path, include
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView


urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list"),

    path("products/<int:pk>/", ProductRetrieveUpdateDeleteView.as_view(), name="product-detail"),
]