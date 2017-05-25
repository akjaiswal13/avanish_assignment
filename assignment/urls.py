"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.home, name="assignment_home"),
    url(r'^task1/', views.assignment_task1, name="assignment_task1"),
    url(r'^task2/', views.assignment_task2, name="assignment_task2"),
    url(r'^task3/', views.assignment_task3, name="assignment_task3"),
    url(r'^task4/', views.assignment_task4, name="assignment_task4"),
    url(r'^task5/', views.assignment_task5, name="assignment_task5"),
    url(r'^task6/(?P<key>.+)/$', views.assignment_task6, name='assignment_task6_key'),
    url(r'^task6/', views.assignment_task6, name="assignment_task6"),
    url(r'^admin/', admin.site.urls),
    url(r'^bigram/', include('bigram.urls')),
]
