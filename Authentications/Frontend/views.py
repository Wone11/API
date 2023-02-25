from django.shortcuts import render

# Create your Front end views here.

def index(request):
    return render(request,'index.html')
