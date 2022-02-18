from multiprocessing import context
from django.shortcuts import redirect, render

from .models import Task 
from .forms import FormTask
from django.http import HttpResponse

# Create your views here.

def formView(request):
    form = FormTask()
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'success')
    
    context = {'form':form}
    return render(request, 'task1/form.html', context)

def success(request):
    return render(request, 'task1/success.html')
    
def userDetail(request):
    detail = Task.objects.all()
    context = {'detail':detail}
    return render(request,'task1/detail.html', context)


