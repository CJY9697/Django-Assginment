"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path,include
from todo.views import todo_list, todo_info, todo_create, todo_update, todo_delete
from users import views as users_views

from fake_db import user_db

_db = user_db


def user_list(request):
    names = [{"id": key, "name": value["이름"]} for key, value in _db.items()]
    return render(request, "user_list.html", {"data": names})


def user_info(request, user_id):
    if user_id > len(_db):
        raise Http404("User not found")
    info = _db[user_id]
    return render(request, "user_info.html", {"data": info})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", user_list, name="user_list"),
    path("users/<int:user_id>/", user_info, name="user_info"),
    path("todo/", todo_list, name="todo_list"),
    path('todo/create/', todo_create, name='todo_create'),
    path("todo/<int:todo_id>/", todo_info, name="todo_info"),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', users_views.login, name='login'),
    path('accounts/signup/', users_views.sign_up, name='signup'),
    path('cbv/', include('todo.urls')),
]