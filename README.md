# Hotel Management  
## Requires  
* Python  
* MySQL(MariaDB) server  
  
## Create DB
1. Login to MySQL(MariaDB) as root  
2. Create DB: `CREATE DATABASE management_db;`  
3. Create user: `CREATE USER 'django_user'@'localhost' IDENTIFIED BY '7529';`  
4. Privileges:  
    `GRANT ALL PRIVILEGES ON management_db.* TO 'django_user'@'localhost';`  
    `FLUSH PRIVILEGES;`

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
