from django.shortcuts import render
from django.http import HttpResponse

def web_content(request):
    return render(request,'TweetAnalysisApp/index.html')