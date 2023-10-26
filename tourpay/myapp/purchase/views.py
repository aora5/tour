from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages
from django.urls import reverse_lazy
# Create your views here.

class purchaseIndex(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "purchase/index.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)
    
class purchaseDetail(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "purchase/detail.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)

class purchaseCancel(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "purchase/cancel.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)