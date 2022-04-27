from django.urls import path
from ..views.category.view import *

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='category_list'),
    path('add/', CreateCategoryView.as_view(),
         name='category_form'),
    path('edit/<int:pk>/',
         CategoryUpdateView.as_view(), name="category_update"),
    path('delete/<int:pk>/',
         CategoryDeleteView.as_view(), name="category_delete"),
    path('form/',
         CatergoryFormView.as_view(), name="category_form")
]
