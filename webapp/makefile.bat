echo Start batch script

python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations training
python manage.py migrate training

python manage.py makemigrations userprofile
python manage.py migrate userprofile

python manage.py makemigrations main
python manage.py migrate main

python manage.py runserver

echo End batch script