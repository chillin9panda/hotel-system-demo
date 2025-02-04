# Hotel Management  
## Requires  
* Python  
* MySQL(MariaDB) server (MariaDB recommended)
  
## Create DB
Login as root and run the SQL commands from [Link Text](management_db.sql "management_db.sql")  
  
## Virtual Environment  
create Virtual environment in project folder: `python -m venv .venv`    
  
#### Activating venv
  
* Windows Bash: `source .venv/Scripts/activate`  
* Linux: `source .venv/bin/activate`  
  
#### Install dependencies in .venv
dependencies from requirements.txt: `pip install -r requirements.txt`  

  
## Create super user  
`python manage.py createsuperuser`  
  
## Run Server  
In project folder in .venv:  
    1. `python manage.py makemigrations`  
    2. `python manage.py migrate`  
    3. `python manage.py runserver 0.0.0.0:8000`  
