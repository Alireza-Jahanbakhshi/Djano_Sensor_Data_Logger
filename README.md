# Djano_Sensor_Data_Logger
In this app,sensor data is shown

Python,html,css,json language and Django framework are used in this project.
Backend:Ali Azamian,Narjes Shagholian,Mahsa Karimian
Frontend:Sara Kabiri,Sina Abdullahi

**Install dependencies:**

> pip install -r requirements.text

**Make migrations:**

> python manage.py makemigrations

> python manage.py migrate

**Run project:**
> python manage.py runserver

**Login : http://194.5.176.138:8000/**
>username : admin
>password : 1234

**Admin : http://194.5.176.138:8000/admin**
>username : admin
>password : 1234

**send data : metod:POST  http://194.5.176.138:8000/api/board/**
>{ "data":"0/148/254/100/1368436083157/27/56/1/0/1/8"}

**get data : metod:GET http://194.5.176.138:8000/api/board/**
