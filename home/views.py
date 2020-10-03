from django.http import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
# from django.template import loader, RequestContext # no longer needed after `revised - simplified` under index
import pandas as pd
import json
import sqlite3

# Create your views here. Used to pass content to the website. (So DB connection and passing variables, etc.)
def index(request):
    testVariable = 'hello world'

    # now pass everything to the webpage, assiging our json to the context dictionary
    context = {'helloWorld':testVariable}
    return render(request,'home/index.html', context)
    # return render(request,'home/indexWithAuth.html', context)

def about(request):
    testVariable = 'hello world'

    # now pass everything to the webpage, assiging our json to the context dictionary
    context = {'helloWorld':testVariable}
    return render(request,'home/about.html', context)


def contact(request):
    testVariable = 'hello world'

    # now pass everything to the webpage, assiging our json to the context dictionary
    context = {'helloWorld':testVariable}
    return render(request,'home/contact.html', context)

