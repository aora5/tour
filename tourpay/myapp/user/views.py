from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import UserCreationForm
# Create your views here.


class userIndex(generic.ListView):
    def __init__(self):
        self.title_nm = "메인페이지입니다."
        self.ogImgUrl = ""
        self.descript = "메인페이지입니다."
        self.template_name = "user/index.html"

    def get(self, request, *args, **kwargs):
        self.content = {"descript": self.descript,
                        "title_nm": self.title_nm,
                        "ogImgUrl": self.ogImgUrl,
                        "dataList": "[[[[ Hellow DJango ]]]]"}

        return render(request, self.template_name, self.content)


class signup(generic.ListView):
    def __init__(self):
        self.title_nm = "회원가입"
        self.ogImgUrl = ""
        self.descript = "회원가입"
        self.template_name = "user/signup.html"

    def get(self, request, *args, **kwargs):
        self.content = {"descript": self.descript,
                        "title_nm": self.title_nm,
                        "ogImgUrl": self.ogImgUrl,
                        "dataList": ""}

        return render(request, self.template_name, self.content)


def login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get('userId')
        password = request.POST.get('userPassword')

        if username and password:
            if not username.isdigit():
                error = '핸드폰 번호는 숫자로만 입력해야 합니다.'
            else:
                user = auth.authenticate(request, username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect('/pay/')
                else:
                    error = '아이디와 패스워드가 일치하지 않습니다.'
        else:
            error = '핸드폰 번호를 입력해주세요.'

    return render(request, 'user/login.html', {'error': error})


def logout(request):
    auth.logout(request)
    return redirect('/user/login.html')



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # 사용자 생성
            return redirect('/pay/')  # 회원가입 성공 시 리다이렉트할 URL
    else:
        form = UserCreationForm()

    return render(request, 'user/signup.html', {'form': form})

    
class firstIndex(generic.ListView):
    def __init__(self):
        self.title_nm       = ""
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "index.html"

    def get(self, request, *args, **kwargs):
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,                                               
                        "dataList":""}

        return render(request, self.template_name, self.content)
    



