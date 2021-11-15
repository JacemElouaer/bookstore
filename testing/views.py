from django.shortcuts import render



def testhome(request):
    return render(request,'testing/testhome.html')
def abouttest(request):
    return render(request,'testing/abouttest.html')
def profile(request):
    return render(request,'testing/profile.html')
def customer(request):
    return render(request,'testing/customer.html')


# Create your views here.
