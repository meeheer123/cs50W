from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request, "hello/index.html")

def mihir(request):
    return HttpResponse("Hello, mihir!")

def greet(request, name):
    # we pass a dictionary as the second argument containing variables for HTML access.
    # remember to send the left as a string
    # if an error shows merge something then check the arguments
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
    })