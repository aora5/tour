from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [    
    path("purchase/", views.purchaseIndex.as_view(), name="구매내역"), 
    path("purchase/detail", views.purchaseDetail.as_view(), name="구매상세"),
    path("purchase/cancel", views.purchaseCancel.as_view(), name="구매취소"),  
]