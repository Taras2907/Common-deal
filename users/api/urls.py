from django.urls import path, include, re_path
from rest_auth import views
from ..api.views import UsernameIsUsedView, EmailIsUsedView

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),

    path('rest-auth/', include('rest_auth.urls')),

    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/password/reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name="password-reset-confirm"),

    path('rest-auth/user/name/', UsernameIsUsedView.as_view(), name="user-exists"),

    path('rest-auth/user/email/', EmailIsUsedView.as_view(), name="email-exists"),

]
