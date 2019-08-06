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
source venv/bin/activate  # enter venv
manage migrate  # setup database
manage runserve
```

# DISCLAIMER
This is my attempt at learning django, so it should be treated as an **experiment** and 
**should definitely not be used for sharing anything important!**