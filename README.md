# AirDnC

A Django note-taking application.

Allows users to create, store and organise their notes.

 
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

astroid==2.0.4
autopep8==1.4
certifi==2018.10.15
chardet==3.0.4
defusedxml==0.5.0
dj-database-url==0.5.0
Django==1.11.15
django-ckeditor==5.6.1
django-forms-bootstrap==3.1.0
django-js-asset==1.1.0
gunicorn==19.9.0
idna==2.7
isort==4.3.4
lazy-object-proxy==1.3.1
mccabe==0.6.1
oauthlib==2.1.0
Pillow==5.3.0
psycopg2==2.7.5
psycopg2-binary==2.7.5
pycodestyle==2.4.0
PyJWT==1.6.4
pylint==2.1.1
python3-openid==3.1.0
pytz==2018.5
requests==2.20.1
requests-oauthlib==1.0.0
six==1.11.0
social-auth-app-django==3.1.0
social-auth-core==2.0.0
typed-ast==1.1.0
urllib3==1.24.1
virtualenv==16.0.0
whitenoise==4.1
wrapt==1.10.11

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