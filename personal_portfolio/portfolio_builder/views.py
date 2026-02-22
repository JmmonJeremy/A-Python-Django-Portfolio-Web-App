from django.shortcuts import render
from django import forms
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.mail import EmailMessage
import base64

# LEARN Create a simple form class that inherits Django's base class for creating forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

# LEARN Home page view passing in request to handle web request (GET, POST, user data, etc.)
def home(request):   
    return render(request, "portfolio_builder/home.html")

# LEARN Form submission view
def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data.get("image")
            processed_image_bytes = None
            if image_file:
                # Open image
                img = Image.open(image_file)
                # Resize image (example: max 800x800)
                img.thumbnail((800, 800))
                # Add watermark
                draw = ImageDraw.Draw(img)
                watermark_text = "Jeremy Suchanski Portfolio"
                # Position bottom right
                width, height = img.size
                draw.text((width - 250, height - 40), watermark_text, fill=(255, 255, 255))
                # Save to memory instead of disk
                image_io = BytesIO()
                img.save(image_io, format="JPEG")
                image_io.seek(0)
                processed_image_bytes = image_io.read()
                encoded_image = base64.b64encode(processed_image_bytes).decode('utf-8')
            name = form.cleaned_data["name"]
            email_address = form.cleaned_data['email']
            message = form.cleaned_data["message"]
            # Send email
            email = EmailMessage(
                subject=f'Portfolio Contact from {name}',
                body=f'From: {name} <{email_address}>\n\nMessage:\n{message}',
                from_email=settings.EMAIL_HOST_USER,             # read from environment,
                to=[settings.EMAIL_HOST_USER],                   # your email           
            )
            if processed_image_bytes:
                email.attach(
                    "watermarked_image.jpg",
                    processed_image_bytes,
                    "image/jpeg"
                )
            email.send()
            success = True
            # Success Message
            form = ContactForm()  # reset form after success
            return render(
                request,
                "portfolio_builder/home.html",
                {
                    "success": True,
                    "name": name,
                    "message": message,
                    "image_data": encoded_image if image_file else None,
                },
            )
    else:
        form = ContactForm()
    return render(request, "portfolio_builder/form.html", {"form": form})
