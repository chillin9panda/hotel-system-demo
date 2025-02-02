CREATE DATABASE management_db;

CREATE USER 'django_user'@'localhost' IDENTIFIED BY '7529';

GRANT ALL PRIVILEGES
ON management_db.* TO 'django_user'@'localhost';

FLUSH PRIVILEGES;
