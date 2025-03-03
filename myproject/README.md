

<<<<<<< HEAD
# Data Americas
=======
# Django Project

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

```bash
python3 -m venv venv
source venv/bin/activate
```

###### Create Superuser
```bash
python3 ./myproject/manage.py createsuperuser
```

###### Db Migrate
```bash
python3 ./myproject/manage.py migrate
```

###### Run the app
```bash
python3 ./myproject/manage.py runserver
```
