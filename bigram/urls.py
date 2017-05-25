from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.bigram, name="bigram_bigram"),
    url(r'task1/$', views.bigram_task1, name="bigram_task1"),
    url(r'task2/$', views.bigram_task2, name="bigram_task2"),
    url(r'task3/$', views.bigram_task3, name="bigram_task3"),
    url(r'task4/$', views.bigram_task4, name="bigram_task4"),
    url(r'task5/$', views.bigram_task5, name="bigram_task5"),
    url(r'task6/$', views.bigram_task6, name="bigram_task6"),
    url(r'^task6/(?P<key>.+)/$', views.bigram_task6, name='bigram_task6_key'),
    
]
