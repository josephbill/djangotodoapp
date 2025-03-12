### To create a django project 
django-admin startproject <nameofapplication>

### how to run a django project 
python manage.py runserver

### DJANGO PROJECT FILES 
1. manage.py :: command line utility allowing us to access 
the django project : entry file 
2. todolist/ : this directory is the actual python django project 
3. __init__.py : this is an empty file that indicates above 
directory is a python project
4. asgi.py :  an entry file for ASGI compatible web servers
to serve your project 
5. wsgi.py :  an entry file for WSGI compatible web servers
to serve your project
6. settings.py : settings/configuration file for the django
project 
7. urls.py : these url declarations that map to our django app. 

### HOW TO CREATE AN APP INSIDE A DJANGO PROJECT
python manage.py startapp <nameoftheapp>

### DJANGO APP FILES 
1. migrations/ : database migration files (empty initially)
2. __init__.py : indicates the app is a python application 
3. admin.py : used to register models for the django admin panel 
4. apps.py : contains the app configurations 
5. models.py : defines the database models (tables)
6. tests.py : contains test cases for the app 
7. views.py : handle request-response logic (functional/controller)
8. urls.py (manually created on app level) : define url patterns 
for the app


### JINJA TEMPLATING 
This is a syntax used to create django interfaces 
- To create templates
  a. Inside the templates you can create .html files , .css , .js 
  b. To consolidate the templating for our project , modify the following 
     - set a global templates directory for referencing our templates i.e. 
       move the  todolist templates folder to the global perspective 
       i.e. root directory level
- register this change in settings.py for the project under the templates directory
  settings 
              'DIRS': [BASE_DIR / 'templates'],  # Add this line



### STEPS TO INCLUDE DB PERSISTENCY FOR PROJECTS IN DJANGO 
models.py : converted to db tables by django 
After defining our models.py 
1/ python manage.py makemigrations appname 
2/ python manage.py migrate 

### STEPS TO ADD A DATA SOURCE 
1. Double click on the db.sqlite3 file 
2. Or simply from pycharm select the database icon 
3. click the + sign or the prompt to create the data source
   (for development use sqlite3)


### RELATION DATABASES : DATABASE RELATIONSHIPS 
1. One to Many Relationship 
    - Taskers table (Contain the users who will perform the tasks)
    - Task table (Contains the tasks)
To establish a one to many relationship establish a ForiengKey
    - a unique key pointing to a unique reference in another db 
   table
2. many to many relationship

### HOW TO ADD IMAGES (STATIC )
1. Django uses static directory 
project-root directory/ => static/ => images/ 
2. Add {% load static %} at the top of the html file 
3. Add this to the settings.py 
STATIC_URL = "/static/"

# Ensure Django knows where to find static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
remember to import OS 























































