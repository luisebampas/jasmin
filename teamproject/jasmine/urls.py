"""config URL Configuration

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
from django.views.generic import TemplateView

from jasmine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='jasmine/home.html'), name='home'),
    path('home',TemplateView.as_view(template_name='jasmine/home.html'), name='home'),

    path('login', views.MainView.login, name='login'),
    path('join', views.MainView.join, name='join'),
    path('joinimpl', views.MainView.joinimpl, name='joinimpl'),
    path('loginimpl', views.MainView.loginimpl, name='loginimpl'),
    path('logout', views.MainView.logout, name='logout'),
    path('mypage', views.mypage, name='mypage'),
    path('userdetail', views.userdetail, name='userdetail'),
    path('userupdate', views.userupdate, name='userupdate'),
    path('userupdateimpl', views.userupdateimpl, name='userupdateimpl'),
    path('userdelete', views.userdelete, name='userdelete'),
    path('orderlist', views.orderlist, name='orderlist'),
    path('cart', views.cart, name='cart'),

    path('mainSection', views.mainSectionView.mainSection, name='mainSection'),
    path('itemlist', views.mainSectionView.itemlist, name='itemlist'),
    path('itemcontent', views.mainSectionView.itemcontent, name='itemcontent'),
    path('payment', views.mainSectionView.payment, name='payment'),
    path('paydetail', views.mainSectionView.paydetail, name='paydetail'),

    path('sideSection', views.sideSectionView.sideSection, name='sideSection'),
    path('category', views.sideSectionView.category, name='category'),

    path('about', TemplateView.as_view(template_name='jasmine/about.html'), name='about'),
    path('map', views.map, name='map'),

]
