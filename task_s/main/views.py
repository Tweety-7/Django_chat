from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from itertools import chain
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
# from django.contrib.auth import is_authenticated
# @login_required(login_url='http://127.0.0.1:8000/login')
from django.db.models import Q

def index(request):
        tasks = ''
        tasks = Task.objects.order_by('-id')

        # tasks = tasks.filter(request.user in [recipient, sponsor])

        # task_pl = list(task_rc, task_sp)
        task_pl = Q(sponsor = request.user)  | Q(recipient = request.user)
        # tasks = task_pl.order_by('-id')
        title = 'Главная страница'
        hrefs = ['logout']
        # title = 'для просмотра, авторизируйтесь'
        # hrefs = ['signup', 'login', 'logout']
        return render(request, 'main/index.html', {'title' : title, 'tasks' : tasks,'hrefs':hrefs})

    # return render(request, 'main/index.html',{
    #     'title': 'Главная страница сайта'})
        # 'tasks':tasks})
# def index(request):
#     return HttpResponse("<h4>main</h4>")


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {'form': form, 'error' : error}
    return render(request, 'main/create.html', context)
def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_my = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_my)
            login(request)
            return redirect('home')
        else:
            error = 'Форма логина заполнена не верно'
    form = UserCreationForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/signup.html', context)
def login(request):
    error=''
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        print("koKoko")
        print(form, form)
        if form.is_valid():
            print("KEK")
            # username = request.POST['username']
            # pas = request.POST['password']
            # username = form.login
            # pas = form.password
            # username = form.cleaned_data.get('username')
            # pas = form.cleaned_data.get('password')
            username = request.POST.get('username')
            pas = request.POST.get('password')
            print(username, pas)
            user = authenticate(username=username, password=pas)
            if user is not None:
                print("УРАААА")
                login(request)
                return  redirect('home')
            else:
                pint("LOL!")
                return redirect('login')

                #{{form.login}}<br>
                #{{forrm.password}}
            # form.confirm_login_allowed()
            # authenticate(form)
        else:
            error='Аккаунт не существует'
            # return render(request,'main/login.html')
    form = AuthenticationForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/login.html', context)

from django.contrib.auth import logout as loogout_1

def logout(request):
    logout_1(request)

def logout_then_login(request):
    pass
