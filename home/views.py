from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("this is about page")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("this is services page")

def contact(request):
    return render(request, "contacts.html")
    # return HttpResponse("this is contacts page")