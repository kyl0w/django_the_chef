from django.shortcuts import render

# Create your views here.
def manager(request):
    return render(request, 'administration/manager/manager.html')

def worker(request):
    return render(request, 'administration/worker/worker.html')