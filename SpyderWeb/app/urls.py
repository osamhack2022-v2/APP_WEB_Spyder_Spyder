# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),
    re_path(r'spyder/upload', views.uploadFile, name='upload'),
    re_path(r'spyder/download', views.downloadFile, name='download'),

    # The home page
    path('', views.index, name='home'),
]
