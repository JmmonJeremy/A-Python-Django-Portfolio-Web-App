from django.shortcuts import render
from django import forms

# LEARN Create a simple form class that inherits Django's base class for creating forms
class PortfolioForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

# LEARN Home page view passing in request to handle web request (GET, POST, user data, etc.)
def home(request):   
    return render(request, "portfolio_builder/home.html")

# LEARN Form submission view
def contact(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            return render(
                request,
                "portfolio_builder/home.html",
                {
                    "success": True,
                    "name": name,
                    "message": message,
                },
            )
    else:
        form = PortfolioForm()
    return render(request, "portfolio_builder/form.html", {"form": form})
