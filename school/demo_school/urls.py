"""demo_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from school.views import *
#CommentsViewSet

from django.contrib import admin
from django.urls import path

#1
#to create a path we need to regiater viewset:
# r = DefaultRouter()
# r.register('comments', CommentsViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Store, name='Store'),
    path('cart/', cart, name='cart'),
    path('update_item/', updateItem),
    path('checkout/', checkout, name='checkout')
#2 add r urls
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

