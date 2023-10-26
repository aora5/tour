from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views


app_name = "user"

urlpatterns = [    
    path("index/", views.userIndex.as_view(), name="main"), 
    path('login/', views.login, name='login'),
    path('signup/', views.signup.as_view(), name='signup'),
    path("", views.firstIndex.as_view(), name="first_index"), 
    ]
