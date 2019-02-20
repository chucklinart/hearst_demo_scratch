## Docker Django setup with custom demo app to store information about courses ##

Assuming you have Docker and docker-compose all set up and running properly and a 
basic knowledge of both:

*You'll need to set up a network in order to run this out of the box.  This is for 
your own protection.*  I called it chuck_network but you can call it whatever you want.
Just be sure to change it in the docker-compose.yml file if you do.

```docker network create chuck_network --subnet 172.24.24.0/24```

*You can run Django commands as follows, eg. to get a Python shell:*

```docker-compose run web /code/manage.py shell```

### Before bringing the app up, you will need to build, migrate and collect static ###

```docker-compose build```

```docker-compose run web /code/manage.py collectstatic```
```docker-compose run web /code/manage.py makemigrations```
```docker-compose run web /code/manage.py migrate```

### Now run the app.###

```docker-compose up```

You will see it in your browser at http://0.0.0.0:8088 

### If you'd like to see the admin section, CTR-C out and create a superuser the normal way, 
then log in at /admin and add some data ###

```docker-compose run web /code/manage.py createsuperuser```

You can see the app hosted on a gunicorn/nginx stack on my server at 

https://hearst-demo.chucklinart.com

I added a RESTful APi at http://hearst-demo.chucklinart.com/api

*Please note that this app is only designed to show that I know my way around Django and can 
create dynamic filters and all that jazz*

