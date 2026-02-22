# Python Django Porfolio Web App

This is a development version of a web app where you can display your work and have people contact you through email if they are interested in hiring you or using your services.

## Instructions for Build and Use

[Software Demo](Put_Your_Video_Link_Here)

Steps to build and/or run the software:

1. Go to the official Python website https://www.python.org/downloads/ and click link to Download Python 3.10 or newer
2. Then double-click the download installer, check the box that says Add Python to PATH, and click Install Now
3. Create a folder to hold the web app and in the terminal of VSCode go to the folder and run the command: py -m venv venv
4. Then to activate the virtual environment, thereby keeping it local, enter the command: .\venv\Scripts\Activate.ps1
5. Install the following 3 packages django, python-decouple, and pillow with the command: pip install
6. Create a django project with the command: django-admin startproject personal_portfolio
7. Change to the personal_portfolio folder with the command: cd personal_portfolio
8. Create the web app structure with the command: python manage.py startapp portfolio_builder
9. In settings.py add to "INSTALLED_APPS" 'portfolio_builder'
10. Follow the steps to setup an email/password connection and .env file in the Steps to Run Program.txt file
11. Copy the code to the various files of the app and replace the information with information about you
12. To start the server run the command: python manage.py runserver
13. To open the web app put the following web address in a browser: http://127.0.0.1:8000/

Instructions for using the software:

1. In VSCode open the folder you created to hold the project and in the VS Code terminal run the command: venv\Scripts\activate
2. Change to the "personal_portfolio" folder with the command: cd personal_portfolio
3. In the VSCode terminal start the server for the web app by running the command: python manage.py runserver
4. Open the following web address in a browser: http://127.0.0.1:8000/
5. Click on the Contact Me button or image, fill out the form, and press the submit button
6. You should recieve an email with the message that was sent through the form and a success message will appear on the home page

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Visual Studio Code
* Python 3.13.7 64-bit
* Django 6.0.2
* pillow 12.1.1
* python-decouple 3.8
* Git / GitHub

## Useful Websites to Learn More

I found these websites useful in developing this software:

### Visual Studio Code :
* [Visual Studio Code & GitHub](https://code.visualstudio.com/docs/sourcecontrol/overview)

### Python :
* [Python Virtual Environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
* [Python Package Requirements](https://learnify.shefali.dev/tutorials/python-requirements-file)
* [BytesIO in Python](https://docs.python.org/3/library/io.html#io.BytesIO)
* [Python base64 docs](https://docs.python.org/3/library/base64.html)
* [Python Base64 Tutorial](https://www.geeksforgeeks.org/python/encoding-and-decoding-base64-strings-in-python/)

### Django :
* [Django Docs Page](https://docs.djangoproject.com/en/5.1/contents/)
* [Django Tutorial](https://www.tutorialspoint.com/django/index.htm)
* [Django Tutorials](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)
* [Django Tutorials](https://www.compilenrun.com/docs/category/django-tutorial)
* [Django App Setup](https://realpython.com/get-started-with-django-1/)
* [Django App Setup](https://web.dataidea.org/Django/02_setup/)
* [Django Cheat Sheets](https://learnbatta.com/course/django/)
* [Django Render](https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/)
* [Django Views](https://docs.djangoproject.com/en/6.0/topics/http/views/)
* [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)
* [Django Templates](https://django.pythonassets.com/docs/templating-system/extending-templates/)
* [Django Forms](https://docs.djangoproject.com/en/6.0/topics/forms/)
* [Django Forms API](https://docs.djangoproject.com/en/6.0/ref/forms/api/)
* [Django CSRF](https://docs.djangoproject.com/en/6.0/howto/csrf/)
* [Django Validation](https://docs.djangoproject.com/en/6.0/ref/forms/validation/)
* [Django Urls](https://docs.djangoproject.com/en/6.0/topics/http/urls/)
* [Django Static](https://docs.djangoproject.com/en/6.0/howto/static-files/)
* [Django Email Docs - EmailMessage](https://docs.djangoproject.com/en/3.2/topics/email/)
* [Django Email Tutorial](https://mailtrap.io/blog/django-send-email/)
* [Gmail with Django SMTP](https://django-tutorial.dev/course/django-for-beginners/how-to/send-email-from-django-server/)
* [Django Email Settings](https://www.geeksforgeeks.org/python/setup-sending-email-in-django-project/)

### Python‑Decouple :
* [Python‑Decouple Doc](https://docs.santoshpurbey.com/django/python-decouple)
* [Python Decouple Usage](https://github.com/HBNetwork/python-decouple)
* [Python Decouple Usage](https://pypi.org/project/python-decouple/)
* []()

### Pillow :
* [Pillow Docs Page](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
* [Pillow Tutorial](https://realpython.com/image-processing-with-the-python-pillow-library/)
* [Pillow Creating Watermark](https://www.geeksforgeeks.org/python/python-pillow-creating-a-watermark/)
* [Pillow Resizing Method](https://www.geeksforgeeks.org/python/python-pil-image-resize-method/)

### CSS :
* [CSS Tutorial](https://www.w3schools.com/css/default.asp)

### Bootstrap 5 :
* [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/ )
* [Bootstrap 5 Tutorial](https://www.w3schools.com/bootstrap5/)
* [Bootstrap 5 Tutorial](https://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-containers.php)

### HTML :
* [HTML Tutorial](https://www.w3schools.com/html/default.asp)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Create a larger more visible watermark on the images
* [ ] Add more projects to the projects secion
* [ ] Create a production version of this web app
* [ ] Create a user sign in to keep information grouped with the user
* [ ] Create a form page to be able to make it user friendly to add the information to the web app through a form
* [ ]
