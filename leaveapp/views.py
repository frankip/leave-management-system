from django.shortcuts import render

# Create your views here.

def index(request):
    title = "Welcome to leave Management App"
    ctx = {
        "title": title
        
    }
    return render(request, 'index.html', ctx)