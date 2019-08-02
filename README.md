# Secret share
Really bare bones private file and URL sharing.

## Installation
```console
python3 -m venv venv  # create venv
source venv/bin/activate  # enter venv
pip install git+https://github.com/przemal/secret_share.git
```

## Usage
```console
python manage.py migrate  # setup database
python manage.py runserve
```

# DISCLAIMER
This is my attempt at learning django, so it should be treated as an **experiment** and 
**should definitely not be used for sharing anything important!**