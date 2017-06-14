'''
Created on Jun 13, 2017

@author: ben
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request,"home.html")