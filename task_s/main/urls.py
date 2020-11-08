from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url



urlpatterns = [
    path('', views.index, name='home'),
    path('about-as', views.about, name = 'about-us'),
    path('create', views.create, name='create'),
    path('signup', views.signup, name='signup'),
    # path('login', views.login, name ='login'),
    # path ('logout', views.logout, name ='logout'),
    # path('logout/', views.logout, name='logout'),
    # url(r"^accounts/", include("django.contrib.auth.urls"))
    # path('logout-then-login', views.logout_then_login, name = 'logout-then-login')

]
