from django.urls import path
from . import views

app_name = "pay"

urlpatterns = [    
path("pay/", views.payIndex.as_view(), name="결제"), 
path("pay/add", views.payAdd.as_view(), name="결제수단등록"), 
path("pay/list", views.payList.as_view(), name="결제수단목록"), 
]