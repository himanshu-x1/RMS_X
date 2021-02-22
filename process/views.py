from django.shortcuts import render
from process.forms import RegistrationForm

# Create your views here.
def showIdex(request):
    return render(request,'process_templates/main.html')


def registration(request):
    print("-------1-------")
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        print("-------3-------")
        if rf.is_valid():
            print("-------4-------")
            #rf.otp = 5475
            print("-------5-------")
            rf.save()
        else:
            return render(request, 'process_templates/registration.html', {"form": rf})
    else:
        print("-------2-------")
        return render(request,'process_templates/registration.html',{"form":rf})



