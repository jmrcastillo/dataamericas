# Data Americas

## Installation Local

Clone the repo
```bash
git clone https://github.com/jmrcastillo/dataamericas
cd dataamericas/myproject
```

[Install Virtualenv & Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)

###### Install Dependencies using Pipenv

```bash
pip install -r ./myproject/requirements.txt
```

###### Install & Activate the virtualenv

``` Create Virtual Environment
python3 -m venv venv
```

``` Activate Virtual Environment
source venv/bin/activate
```


###### Create PostgresDB
```bash
add to .env postgreDB details

Default is sqlite
```

###### Db Migrate
```bash
python3 ./myproject/manage.py makemigrations
python3 ./myproject/manage.py migrate
```

###### Create Superuser
```bash
python3 ./myproject/manage.py createsuperuser
```

###### Run the app
```bash
python3 ./myproject/manage.py runserver
```
