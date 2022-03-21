## Run server for Windows:

1 - create venv 
```
python -m venv ./venv
```
2 - activate venv
```
venv\Scripts\activate.bat
```
3 - install requirements.txt
```
pip install -r requirements.txt
```
4 - create .env file
```
copy example.env .env
```
5 - migrate
```
python manage.py makemigrations
python manage.py migrate
```
6 - runserver
```
python manage.py runserver
```