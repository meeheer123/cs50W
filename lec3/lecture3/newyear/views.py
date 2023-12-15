from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    today = str(date.today())
    res = False
    year, month, day = today.split("-")
    if (month == '1' and day == '1'):
        res = True
    else:
        res = False
    # remember to send the left as a string
    # if an error shows merge something then check the arguments
    return render(request, "newyear/index.html", {
        "newyear": res
    })