
from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [

    path('', ProductsList.as_view(), name='products'),
    path('<int:pk>/', ProductDetail.as_view(), name='product'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),

]
