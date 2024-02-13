from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('fruits/', views.fruits, name='fruits'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]
