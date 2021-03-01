from django.shortcuts import render,redirect
from process.forms import RegistrationForm
from process.models import RegistrationModel

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

            rf.save()
            return redirect('user-otp')
        else:
            return render(request, 'process_templates/registration.html', {"form": rf})
    else:
        print("-------2-------")
        return render(request,'process_templates/registration.html',{"form":rf})


def user_OTP(request):
    return render(request,"process_templates/otp.html")


def validate_otp(request):
    try:
        result = RegistrationModel.objects.get(contact=request.POST.get("t1"),otp=request.POST.get("t2"))
        if result.status == "pending":
            result.status = "approved" #updating
            result.save() #saving
            return redirect('conformation')
        else:
            pass
    except RegistrationModel.DoesNotExist:
        print("Invalid")
    return None


def conformation(request):
    return render(request,"process_templates/conformation.html")