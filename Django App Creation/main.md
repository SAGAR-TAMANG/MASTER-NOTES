Steps I've prepared:

- install pipenv, django, pillow (for image in database)
- run "pipenv install"
- start django project by using "django-admin startproject project_name ."
  - the period at the end suggests that the project shall be created inside the current directory.
- run a server
  - either do django-admin runserver
    - this might not work because settings are not configured inside the manage.py 
  - or do "python manage.py runserver 9000"
    - here, 9000 is the port number; by default 8000
- run the python present inside the virtual env:
  - "Ctrl + Shift + P" then search "Python: Select interpreter" 
  - Paste the virtual environment path inside it and add "/bin/python" at the end
- check out the installed apps inside the settings.py
  - you can remove apps you don't want
- create an app using the command "python manage.py startapp anyrandomname"
  - just add the name inside the original settings.py

# Creating a view: A request handler
- views.py inside the newly created application
- create the functions there which the user will call as a request

# Configuring a URL for the users to access the functions you just created
- create url.py (name can be changed) where you will put all the urls together inside the newly created app
- inside that url.py, you will configure the URLs.

# Sending a dictionary through 'views.py' in order to use it inside the html 
- generally django is not used to create html like that in back, only for example it's showing that

# Putting aside the Models
- 

# Working with templates
- Integrating the sending of dictionary values from views.py while calling the views.
- Integrating an html instead of creating the html on demand using HttpResponse
  - Creating a templates directory at the root.
  - Adding the template directory name in the DIR part of the Templates of the settings.py
- Integrating two htmls together
  - By creating another base html (base i.e. same for all)
  - Adding jinja's {%  %} inside the htmls

# Using GET Http Method: (Example: Addition of two numbers)
- First, create one <form> that takes inputs with input type as "submit", 
- The <form> should have "add" as the action, so the URL can recognize and call the "add"
- The URL should point towards the views (User made function).
- Create a function inside the view, that does the addition and send the output to a result.html. 

# Using POST Http Method:
- First, inside the <form> add a word "method='POST'"
- Then, in the <form> add a jinja i.e., {% csrf_token %},
  - This specifies that our html will use csrf to avoid any attacks
- Then finally, change our function's (one inside the views.py) from GET to POST

# Seperation of Concerns
- Data, Layout, and Logic
## MVT/ MTV Template
- Model View Template
- Data is linked to Model
- DTL:
  - Django Template Language
- User<-->Django<-->URL<-->Views<-->Model & Template
                                    Model<-->Data
- MVC (Model View Controller)

# Using an index.html i.e., template (HTML/CSS/JS) downloaded from web:
- First, put your index.html or other htmls that you will call on views into a template folder.
  - Any folder you keep, it should be a template as defined inside the main setting.py.
- Then, all the files that are required, like CSS, images, etc, of the HTML, keep it somewhere defined (Eg: Template).
- Go to the main settings:
- At the bottom, below the STATIC_URL add: 
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'telusko/static') #Where the other files (folder for index.html) can be found
  ]
  STATIC_ROOT = os.path.join(BASE_DIR, 'assets') # Here, assets is just a name where Django will put our static files
- Then, go to the HTML you have, for us it's index.html, and in every path (eg: <a href="PATH") add one thing:
  - {% static 'PATH' %} # At every PATH mentioned in the HTML
- {% load static %} # Also add this at the top of the HTML 
- Then run: python manage.py collectstatic

# Creating object models to send multiple values together:
- Create a file named models.py inside the app, if it's not created already (for our example: it's travel)
- Inside the model, define a class with as many properties as you want.
- These values will later be imported and called inside the views.
- Then the views will send these to the HTML
- From the HTML side you can receive the definite class and use the values of it.
- You can create a short form for the phrase {% static = "folder" %}
  - By mentioning this at the top of the code: 
    {% static "folder" as WhateverURL}
- How to use for loop or if else statement?
  - For Loop:
    {% for thing in thing %}
    # Jargon Code
    {% endfor %}
  - if else:
    {% if thing == thing %}
    # Jargon Code
    {% endif %}

# Object Relatinal Mapping (ORM)
- install "mysqlclient" for the Django to use MySQL
- Inside the models.py change your normal class into a model by adding this:
  - Normal Class:
  class MyClassName:
    name: str 
    price: int
  - Converted into a model:
  class MyClassName(models.Model): # Find Details in "Django Model Field Reference" in Google
    name= models.CharField(max_length=50)   # Notice how ':' has been changed to '='
    price= models.IntegerField(max_length=10)
- Run "python manage.py makemigrations" # Applying Migrations

# Creating a Super User in order to use "localhost:8000/admin" i.e. admin of our django
- Run "python manage.py help" # In case you want to know the command
- Run "python manage.py createsuperuser 

# Admin Panel: (You (users) can view or modify the databases)
- Go to the Admin URL, and log on using your super user id
- If you get 'Model class django.contrib.sessions.models.Session' Error:
  - Then put 'django.contrib.session' inside the INSTALLED_APPS sections of settings.py
- If you get 'ProgrammingError at /admin/login/ (1146, ".django_session' doesn't exist")'
  - Then you just forgot to migrate the sessions (the app you wrote in the INSTALLED_APPS sections)
  - So, write, 'python manage.py migrate' 
- Now, inside the 'MyApp/admin.py' you list/register your model there by passing the following code:
  - from .models import MyModelName
  - admin.site.register(MyModelName)

# Add and Fetch data from a Database:
- # Adding a default path (URL) for media: 
  - put this in the settings:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  - Go to the urls.py, and add a new urlpatterns:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
# Steps to create a personal command in Django
- Create the following folders in an app of your choice '/management/commands/'
- Create a file command_name.py
  - Alert: Choosing a custom command name is really really important as you will be calling it again and again
- Write the code to create a Command class:
- You may add Custom options as well
 

Few Commands for pipenv:
- "pipenv --venv"
> To view the address of the virtual environment.

