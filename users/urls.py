from django.urls import path
from . import views

##'' значит переход при пустой страничке (первый аргумент '') переходит на этот адрес
    ##"Второй аргумент это функция для возврата реквеста"""
    ###НЕ ЗАБУДЬ В SETTING ПРОПИСАТЬ ДЛЯ МОДУЛЯ ПУТЬ В INSTALLED APPS####

app_name = "users"
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('login/', views.logout_user, name='logout'),
]