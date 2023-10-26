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

class payIndex(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "pay/index.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)

class payAdd(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "pay/add.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)

class payList(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "pay/list.html"

    def get(self, request, *args, **kwargs):        
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                       
                        "dataList":""}

        return render(request, self.template_name, self.content)