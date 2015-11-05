# dragcms

##It is a cms with ability to drag around titles, content(text), link youtube videos and show images.

##It is linked up to a django backend which allows it to save.

##To set up the project

* Create a new folder called "dragcms"
* cd dragcms
* Use "virtualenv -p python3 env" for Python3 virtualenv
* use "source env/bin/activate" for env
* Clone the repo
* cd dragcms
* "pip install -r requirements.txt" to download Django and PostgreSQL
* In settings.py change the database to
```python
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
```
* for sqlite (much easier to set up for development)
* Then run "python manage.py makemigrations"
* Then run "python manage.py migrate"
* Then run "python manage.py runserver"
* Go onto localhost (http://127.0.0.1:8000/)
* After that you should be able to create an article and create sections for it
* To get to the admin section go to (localhost/article/admin/)
