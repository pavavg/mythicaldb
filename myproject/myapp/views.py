# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    text = """ <h1> welcome to my app! MADAFAKA </h1> """
    return HttpResponse(text)
# Create your views here.
