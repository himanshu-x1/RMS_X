from django.shortcuts import render

# Create your views here.
def showIdex(request):
    return render(request,'index.html')