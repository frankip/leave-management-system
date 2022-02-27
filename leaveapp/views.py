from django.shortcuts import redirect, render

# local imports
from .models import Leave
from .forms import LeaveForm

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


def requet_new_leave(request):
    # add form funtionality here
    if request.method == 'POST':
        # create form instance and populate with data from htmls forms 
        form = LeaveForm(request.POST)
        # validate the inputs
        if form.is_valid():
            # form.commit(False)
            form.save()
            return redirect('leaves')

    # instantiate empty form
    form = LeaveForm()
    ctx={
        'form': form
    }
    return render(request, 'request_leave.html', ctx)

def delete_leave_request(request, id):
    deleted = Leave.delete_single_data(id)
    print('deleted', deleted)
    return redirect('leaves')

# figure out how to get the date diference
