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
remember to import OS ''

### DJANGO ADMIN 
Create a super user for content management purposes 
1. Register your models in admin.py 
2. Creating a super admin user for the project 

python manage.py createsuperuser 
3. Visit the link appurl/admin - use the superuser credentials to login

### DJANGO APIS (APPLICATION PROGRAMMING INTERFACE)
Is a set of rules that allows different software apps to 
communicate with each other 
#### Think of an API as a waiter in a restaurant 
1. You(Frontend/client) make an order(request)
2. The waiter(API) takes the request to the kitchen(server/backend)
3. The kitchen(server) prepares the food(process the request)
4. The waiter(API) brings back the meal(response) to you 
### TYPES OF APIS 
1. REST API  => Uses HTTP methods ::
- GET :: use this to request data from servers (default)
- POST :: use this to save or send data to servers 
- PUT :: use this to update on data on servers 
- PATCH :: use this to update only a section of your data 
- DELETE :: use this to remove data from your servers 
2. GraphQL API => Allows clients/frontend to access data only when needed
3. SOAP API => Uses XML methods / older (secure)
4. WebSocket API => Enable real time data transfer (chat applications)
### Steps to create an API project in DJANGO 
1. Install djangorestframework :: pip install djangorestframework 
2. Add djangorestframework as part of the installed apps 
3. Have views return data as .json files 
### JSON (JavaScript object notation)
This is an interchangeable data format that can be used across any 
application 

 python manage.py startapp todolistappapi
 pip install djangorestframework
 pipx install djangorestframework


FrontEnd(HTML <CSS (web) , Android(Jetpack compose) , React Native ,
Reactjs)
=> middleware => backend (server scripting(python->django), database)































































