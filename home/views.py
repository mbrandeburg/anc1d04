from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
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




# def detail(request, question_id):
#     ## original:
#     # return HttpResponse("This is the detailed view of the question: {}".format(question_id))
    
#     ## revisied:
#     question = get_object_or_404(Question, pk=question_id)
#     selected_choice = request.POST['choiceTA3']
#     # wont pass in variabvle with dictionary this time..just gunna code the dictionary inside
#     return render(request, 'polls/detail.html', {'question':question})
