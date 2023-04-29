from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def questions(request):
    return render(request, 'main/questions.html')