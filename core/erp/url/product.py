from django.urls import path
from ..views.product.view import *

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('form/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
]
