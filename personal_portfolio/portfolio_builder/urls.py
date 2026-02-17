from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # LEARN
    path("contact/", views.contact, name="contact"),
]
