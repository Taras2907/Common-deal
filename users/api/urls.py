from django.urls import path, include
from rest_auth import views

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),

    path('rest-auth/', include('rest_auth.urls')),

    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/password/reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),




]