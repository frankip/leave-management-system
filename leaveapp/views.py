from django.shortcuts import render
from .models import Leave

# Create your views here.

def index(request):
    title = "Welcome to leave Management App"
    ctx = {
        "title": title
        
    }
    return render(request, 'index.html', ctx)

def fetch_all_leaves(request):
    all_leave = Leave.fetch_all_data()
    ctx = {
        "all_leave":all_leave
    }

    return render(request, 'leave.html', ctx)


def fetch_leave_details(request, id):
    leave_details = Leave.fetch_single_data(id)

    ctx = {
        "leave_details": leave_details
    }

    return render(request, 'leave_details.html', ctx)