from django.shortcuts import render
from process.forms import RegistrationForm

# Create your views here.
def showIdex(request):
    return render(request,'process_templates/main.html')


def registration(request):
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        pass
    else:
         return render(request,'process_templates/registration.html',{"form":rf})