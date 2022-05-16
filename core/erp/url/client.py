from django.urls import path
from ..views.client.client import *


urlpatterns = [
    path('list/', ClientView.as_view(), name='client'),
]
