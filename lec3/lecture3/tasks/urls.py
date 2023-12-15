from django.urls import path
from . import views

# this allows us to avoid namespace collision
# namespace collision occurs when we have 2 urls.py files with same name attribute
app_name = "tasks"
urlpatterns =  [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]