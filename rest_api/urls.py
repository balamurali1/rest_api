"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app1.views import CategoryAPIView,ProductAPIView,SalesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/',CategoryAPIView.as_view()),
    path('categories/<int:cat_id>/',CategoryAPIView.as_view()),


    path('product/',ProductAPIView.as_view()),
    path('product/<int:pro_id>/',ProductAPIView.as_view()),


    path('salesorder/',SalesAPIView.as_view()),
    path('salesorder/<int:sal_id>/',SalesAPIView.as_view()),




]
