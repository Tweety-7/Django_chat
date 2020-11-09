from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_l
from itertools import chain
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.contrib.auth.hashers import make_password


def index(request):
        tasks = ''
        if request.user.is_active:
            tasks = Task.objects.order_by('-id')
            tasks = tasks.filter(Q(sponsor = request.user)  | Q(recipient = request.user))
        # tasks = tasks.filter(request.user in [recipient, sponsor])


        title = 'Главная страница'
        hrefs = ['logout']
        # title = 'для просмотра, авторизируйтесь'
        # hrefs = ['signup', 'login', 'logout']
        return render(request, 'main/index.html', {'title' : title, 'tasks' : tasks,'hrefs':hrefs})




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
            print('KOK')
            print(user)
            print('KOK')
            login_l(request, user)
            return redirect('home')
        else:
            error = 'Форма логина заполнена не верно'
    form = UserCreationForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/signup.html', context)
def login(request):
    error=''
    if request.method == 'POST':
        form = AuthenticationForm(None, request.POST)
        # 'AuthenticationForm' object has no attribute 'cleaned_data'
        # username = form.cleaned_data.get('username')
        # password_my = form.cleaned_data.get('password')
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        print('form!!', form)
        if form.is_valid():
            print("UUU")
            user = form.get_user()
            login_l(request, user)
            return redirect('/')

        # print(form.valid)
        # print(form.valid())


        # print('is_valid^!',form.is_valid)
        # print('is_valid()!',form.is_valid())
        #
        # print('1 username', form['username'])
        #
        # user = form.get_user()
        # print('GU()!',user)
        # print('GU_',form.get_user)

        # login_l(request, user)

        # user.authenticate()
        # user = authenticate(form.get_user())
        # auth_login(request, form.get_user())
        # login_l(request, user)
        # print(user)
        # if user is not None:
        #         print('KOK')
        #         login_l(request, user)
                # return redirect('home')

        # else:
        #     print('KEK')
        #     error = 'Ошибка заполнения формы('
            # return redirect('login')

    form = AuthenticationForm()
    context = {'form' : form, 'error' : error}
    return render(request, 'main/login.html', context)


from django.contrib.auth import logout as lout
def logout(request):
    lout(request)
    return  redirect('/')
#
# def logout_then_login(request):
#     pass
