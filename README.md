# AirDnC [![Build Status](https://travis-ci.com/davedodea/CI-Project5.svg?token=mSbTyy1sJpCTYfpkhqUw&branch=master)](https://travis-ci.com/davedodea/CI-Project5)

A Django note-taking application.

Allow users to create, store and organise their notes.

 
## UX
This application is built with a mobile first, responsive design.

## Features
TODO
### Existing Features
TODO
### Features Left to Implement
TODO
## Technologies Used
- [Bootstrap](https://getbpptstrap.com)
    - Bootstrap is used as the primary CSS framework

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
    - Also used for asynchronous HTTP (Ajax) requests.

- [Django](https://www.djangoproject.com/)
    - MVT (Mode-View-Template) framweork used to build the application. 

- [PostgreSQL](https://www.postgresql.org/)
    - Relational database store for model data.

## Testing

TODO

## Deployment
- The Django application and the PostgreSQL database are deployed to seperate Heroku instances.

- Deployments are triggered via the pipeline connected directly to the master branch of the GitHub repository.

- Ensure you have set the following config vars set in Heroku settings:
    - `DATABASE_URL`
    - `EMAIL_ADDRESS`
    - `EMAIL_PASSWORD`
    - `SECRET_KEY` (arbitrary string)

    For Social auth:
    - `SOCIAL_AUTH_GITHUB_KEY`
    - `SOCIAL_AUTH_GITHUB_SECRET`


## Install locally

- Clone the repository

- Activate a virtual environment

- CD into the repository

- Install requirements: `pip install -r requirements.txt`

- Ensure you have set the following environment variables:
    - `DATABASE_URL`
    - `EMAIL_ADDRESS`
    - `EMAIL_PASSWORD`
    - `SECRET_KEY` (arbitrary string)

    For Social auth:
    - `SOCIAL_AUTH_GITHUB_KEY`
    - `SOCIAL_AUTH_GITHUB_SECRET`

- Make migrations: `python3 manage.py makemigrations`

- Migrate: `python3 manage.py migrate`

- Run the server: `python3 manage.py runserver`

```python
requirements.txt

algoliasearch==1.19.1
algoliasearch-django==1.7.0
asn1crypto==0.24.0
astroid==2.0.4
autopep8==1.4
Brlapi==0.6.6
certifi==2018.11.29
chardet==3.0.4
chrome-gnome-shell==0.0.0
command-not-found==0.3
cryptography==2.1.4
cupshelpers==1.0
defer==1.0.6
defusedxml==0.5.0
distro-info==0.18
dj-database-url==0.5.0
Django==1.11.15
django-forms-bootstrap==3.1.0
django-js-asset==1.1.0
gunicorn==19.9.0
hidpidaemon==18.4.4
httplib2==0.9.2
idna==2.8
isort==4.3.4
jsonfield==2.0.2
kernelstub==3.1.0
keyring==10.6.0
keyrings.alt==3.0
language-selector==0.1
lazy-object-proxy==1.3.1
louis==3.5.0
macaroonbakery==1.1.3
mccabe==0.6.1
netifaces==0.10.4
oauthlib==2.1.0
olefile==0.45.1
pep8==1.7.1
pexpect==4.2.1
Pillow==5.3.0
protobuf==3.0.0
psycopg2==2.7.5
psycopg2-binary==2.7.5
pycairo==1.16.2
pycodestyle==2.4.0
pycrypto==2.6.1
pycups==1.9.73
pydbus==0.6.0
pygobject==3.26.1
PyJWT==1.6.4
pylint==2.1.1
pymacaroons==0.13.0
PyNaCl==1.1.2
pyRFC3339==1.0
python-apt==1.6.3
python-xlib==0.20
python3-openid==3.1.0
pytz==2018.7
pyxdg==0.25
PyYAML==3.12
Repoman==1.0.2
reportlab==3.4.0
requests==2.21.0
requests-oauthlib==1.0.0
requests-unixsocket==0.1.5
SecretStorage==2.3.1
sessioninstaller==0.0.0
six==1.12.0
social-auth-app-django==3.1.0
social-auth-core==2.0.0
system-service==0.3
systemd-python==234
typed-ast==1.1.0
ubuntu-drivers-common==0.0.0
ufw==0.35
urllib3==1.24.1
virtualenv==16.0.0
whitenoise==4.1
wrapt==1.10.11
xkit==0.0.0


```


## Credits
TODO
### Acknowledgements
- Social buttons for Bootstrap:
   - https://github.com/lipis/bootstrap-social

- Hover CSS:
   - https://github.com/IanLunn/Hover

### Content
TODO
### Media
TODO
