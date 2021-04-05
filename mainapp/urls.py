from django.urls import path

from mainapp.views import BaseView, ProductDetailView, CategoryDetialView, CartView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetialView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart')
]
