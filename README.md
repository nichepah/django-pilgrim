apt-get install python3-django
django-admin --version

Reference: Django Documentation, Release 4.0.dev20210603072047

-----
django-admin startproject mydjango1
python manage.py createsuperuser
python3 manage.py runserver 8081

./manage.py startapp myApp

After models are edited, run 
manage.py makemigrations myApp

manage.py migrate
-----------
MVC - Model-View-Controller strategy

within mydjango1/mydjango1
			__init__.py
			admin.py
			settings.py
			urls.py
			wsgi.py		
			migrations/
			
			
Running django with gunicorn
	gunicorn, a python http server for WSGI apps
	heroku, dyno
	load and resource balancing
			
To start develop server
./manage.py runserver 8080

To create app under a project
./manage.py startapp myApp

After creating models.py and urls.py in myApp
./manage.py migrate 

To capture a value from the URL, in the urlconf, use angle brackets
These patterns are tested in order.

	Eg: 
	from django.urls import path
	from . import views
	urlpatterns = [
	path('articles/2003/', views.special_case_2003),
	path('articles/<int:year>/', views.year_archive),
	path('articles/<int:year>/<int:month>/', views.month_archive),
	path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
	]
	
In forms.py
	message = forms.CharField(widget=forms.Textarea)

--


git remote add origin https://github.com/nichepah/django-pilgrim.git
