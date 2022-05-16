from django.urls import path, include
from .views.category.view import *
from .views.dashboard.view import *
app_name = "erp"

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('category/', include('core.erp.url.category')),
    path('product/', include('core.erp.url.product')),
    path('client/',include('core.erp.url.client'))
]
