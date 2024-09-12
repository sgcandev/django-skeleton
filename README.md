## Installation


```bash

# create virtualenv
python -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# copy environment
cp .env.example .env

# run migrations 
./manage.py migrate

# run server 
./manage.py runserver
```

## Aditional commands


```bash

# format code
black .
black src/apps/users

# loaddata
./manage.py loaddata {fixture_name}
./manage.py loaddata document_sort document_state

# create new app
mkdir -p src/apps/{app_name}
./manage.py startapp {app_name} src/apps/{app_name}

mkdir -p src/apps/documents
./manage.py startapp documents src/apps/documents
```