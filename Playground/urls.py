from django.urls import path
from . import views

# URLconfig for Playground app
urlpatterns = [
    path('hello/', views.say_hello),
]