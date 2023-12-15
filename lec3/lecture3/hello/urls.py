from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # this takes a url, function, name to reference it later
    path("mihir", views.mihir, name="mihir"),
    # we give which url this is [here we dont know so we have written a string]
    # the value after str: should be same as the parameter in greet function
    path("<str:name>", views.greet, name="greet")
]