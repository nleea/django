from django.urls import path
from .views.category.view import *

app_name = "erp"

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CreateCategoryView.as_view(), name='category_form'),
    path('category/edit/<int:pk>/',
         CategoryUpdateView.as_view(), name="category_update"),
    path('category/delete/<int:pk>/',
         CategoryDeleteView.as_view(), name="category_delete")
]
