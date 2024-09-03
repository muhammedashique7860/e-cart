"""
URL configuration for e_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from . import views 
from .views import logout_view 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/',views.Hpage,name='home_page'),
    path('',views.Index,name='index'),

    path('signup',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout', logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
     #add cart 



    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


    # contact page

    path('contact_us',views.Contact_page,name='contact_page'),
    

    # check out page
    path('checkout/',views.CheckOut,name="checkout"),

    # order page

    path('order/',views.Your_Order,name='order'),
    

    # product page

    path('product/',views.Product_page,name="product"),

    # product detail

    path('product/<str:id>',views.Product_detail,name="product_detail"),


    # search 
    path('search/',views.Search,name="search"),



]+ static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)


