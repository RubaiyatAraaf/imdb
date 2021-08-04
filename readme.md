# imdb
Django IMDB.
A movie and celebrity info website.

Used technology:

Django (Python) + Jquery, Bootstrap
Please follow the process below to install

Clone this repository use: 
     git clone https://github.com/RubaiyatAraaf/imdb.git
 
Cd to folder:
    
    cd imdb/

setting up a development environment.start an environment with requirements e.g. 
    pipenv install -r /requirements.txt

migrating the already defined models and creating the super user

    python manage.py migrate

super user should be created before the dummy data be loaded!

    python manage.py createsuperuser

loading dummy data

    python manage.py loaddata data.json

collectstatic -> required/needed for ckeditor (wysiwyg editor)

    python manage.py collectstatic

P.S: you may follow the process as the ordering defined or there may be problems with user related data

Version History:
0.0.1



