from django.shortcuts import render
from django.http import HttpResponse


def analyze_sentence(request):
    return render(request,'index.html')