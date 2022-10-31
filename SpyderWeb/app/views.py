# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from models import *
import os
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

import numpy as np
import cv2
import imutils
import datetime

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        camera = cv2.imread(uploadedFile) 
        gun_cascade = cv2.CascadeClassifier('cascade.xml')
        
        firstFrame = None
        gun_exist = False

        while True:
            
            ret, frame = camera.read()
        
            frame = imutils.resize(frame, width = 500)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            gun = gun_cascade.detectMultiScale(gray,
                                            1.3, 5,
                                            minSize = (100, 100))
            
            if len(gun) > 0:
                gun_exist = True
                break
        
        # Saving the information in the database
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile,
            gun_exist=gun_exist
        )
        document.save()

    documents = models.Document.objects.all()

    return HttpResponse("success")

def downloadFile(request):
    fileName = request.POST["filename"]
    file_path = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/" + fileName)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment;'
    return response