from django.urls import path
from . import views

app_name = "package"

urlpatterns = [    
path("package/", views.packageIndex.as_view(), name="단체"), 
path("package/list", views.packageList.as_view(), name="단체목록"), 
path("package/option", views.packageOption.as_view(), name="옵션"), 
path("package/payment", views.packagePayment.as_view(), name="옵션결제"), 
]