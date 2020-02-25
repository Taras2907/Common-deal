"""common_deal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('users.api.urls')),

    path('api/', include('products.api.urls')),

    # re_path(r'^.*$', TemplateView.as_view(template_name='application.html'), name="entry-point"),
    path('', TemplateView.as_view(template_name='application.html'), name="entry-point"),

    # path('offers/', include('offers.urls')),
    # path('products/', include('products.urls')),
    # path('users/', include('users.urls')),
    # path('search/', include('search.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*$', TemplateView.as_view(template_name='application.html'), name="entry-point")]
