
from django.urls import path
from .view.views import *

app_name = 'auth'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup')
]
