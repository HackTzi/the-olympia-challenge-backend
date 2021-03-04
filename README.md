# Jipeek API 👨‍💻
To make the api run in a local environment you must follow the following steps you must take into account that this, guide is made for linux operating systems like Ubuntu or similar.
## What you need 🙋
- python3.6 or higher
- pip3 
- postgresql 10 or higher
- docker (optional)
## Prerequisites 📄
Update and upgrade your O.S
`sudo apt-get update` and `sudo apt-get upgrade`

### How to install python3 ⬇️
Go to the terminal and execute the next command

`sudo apt install python3`

Run python to make sure it's installed `python3`

### How to install pip3 ⬇️
Go to the terminal and execute the next command
`sudo apt install python3-pip`

Run the following command to make sure pip is installed 

`pip3 --version`

### How to install postgreSQL ⬇️
To install postgreSQL you must use the following instructions
Go to the terminal and execute the next command

1. Install certificates and import GPG repository key
`sudo apt-get install wget ca-certificates` and `wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`

2. Add the PostgreSQL
`sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ lsb_release -cs-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'`

3. Update the package list 
`sudo apt-get update`

4. Install postgreSQL
`sudo apt-get install postgresql postgresql-contrib`

5. Check Available PostgreSQL Version `apt show postgresql`

6. Install PostgreSQL packages `sudo apt install postgresql postgresql-contrib`

## Run application 🚀
1. Clone repo using git or download
2. Install dependence's `pip3 install -r requirements.txt`
3. Create database in postgresql 
    ```
    sudo su - postgres
    psql
    \password postgres #pick a password for the postgres role
    CREATE DATABASE connectcare;
    ```
4. Configure database into connectcare/settings.ini
    ```
    [settings]
    SECRET_KEY=<your_secret_key>
    DEBUG=<True or False>
    DATABASE_NAME=<your_db_name>
    DATABASE_USER=<your_db_user>
    DATABASE_PASSWORD=<your_db_password>
    DATABASE_HOST=<your_db_host>
    DATABASE_PORT=5432
    ```

5. Run migrations and run server `python3 manage.py migrate` and `python3 manage.py runserver`

6. Go to [127.0.0.1:8000](http://127.0.0.1:8000)

## Run application with Docker 🐋
You can install the docker using the following guides:
- [Intall docker engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/ "Install docker engine on Ubuntu")
- [Intall docker-compose](https://docs.docker.com/compose/install/)

### Configure database into connectcare/settings.py
```
[settings]
    SECRET_KEY=<your_secret_key>
    DEBUG=<True or False>
    DATABASE_NAME=postgres
    DATABASE_USER=postgres
    DATABASE_PASSWORD=postgres
    DATABASE_HOST=db
    DATABASE_PORT=5432
```

### Services 📦
- db : potgreSQL : port 5432 (docker network)
- web : Python3 Linux Alpine : port 8080

### Useful commands
- build containers and download images `docker-compose build`
- start services `docker-compose up`
- down services `docker-compose down`
- execute manage.py command `docker-compose run --rm web python3 manage.py <command>`