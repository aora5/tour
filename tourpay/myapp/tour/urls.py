from django.urls import path
from . import views

app_name = "tour"

urlpatterns = [    
path("tour/", views.tourIndex.as_view(), name="행사"), 
path("tour/add-qr", views.tourAddqr.as_view(), name="행사추가"),
path("tour/add-code", views.tourAddcode.as_view(), name="행사추가"),
path("tour/check", views.tourCheck.as_view(), name="행사추가"),
path("tour/sc-check", views.scheduleCheck.as_view(), name="행사추가"),
]