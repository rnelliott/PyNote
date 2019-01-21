# AirDnC [![Build Status](https://travis-ci.com/davedodea/CI-Project5.svg?token=mSbTyy1sJpCTYfpkhqUw&branch=master)](https://travis-ci.com/davedodea/CI-Project5)

A modern note-taking application. Built with Python and the Django framework.

Allow users to create, store and organise their notes.

 
## UX
This application is built with a mobile first, responsive design in mind

## Features
- Full user account system for authenticaion.
- Social sign-on for GitHub, Twitter and Google.
- Users may create, store and organise the notes.
- Categorise user notes.
- Full search via notes and categories.
- Payment plans via Stripe credit card payment processing.

### Features Left to Implement
- Sharable notes to public.
- Sharable notes to other registered users.
- Tags for notes.

## Technologies Used
- Python
- JavaScript
- HTML
- CSS

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
    - Also used for asynchronous HTTP (Ajax) requests.

- [Django](https://www.djangoproject.com/)
    - MVT (Mode-View-Template) framweork used to build the application. 

- [PostgreSQL](https://www.postgresql.org/)
    - Relational database store for model data.
    
- [Heroku](https://www.heroku.com/)
    - Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
    
- [Bootstrap](https://getbpptstrap.com)
    - Bootstrap is used as the primary CSS framework.

## Deployment
- The Django application and the PostgreSQL database are deployed to seperate Heroku instances.

- Testing is triggered via TravisCI upon PR's to the GitHub repository.

- Once TravisCI builds, deployment is carried out on Heroku.

- If you wish to deploy - ensure you have set the following config vars set in Heroku app settings:
    - 'DATABASE_URL'
    - 'EMAIL_ADDRESS
    - 'EMAIL_PASSWORD'
    - 'SECRET_KEY' (arbitrary string)
    - 'DATABASE_URL'
    - 'EMAIL_ADDRESS'
    - 'EMAIL_PASSWORD'
    - 'SECRET_KEY'
    - 'SOCIAL_AUTH_GITHUB_KEY'
    - 'SOCIAL_AUTH_GITHUB_SECRET'
    - 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'
    - 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'
    - 'SOCIAL_AUTH_TWITTER_KEY'
    - 'SOCIAL_AUTH_TWITTER_SECRET'
    - 'STRIPE_PUBLISHABLE'
    - 'STRIPE_SECRET'
    
## Install locally

- Clone the repository

- Activate a virtual environment

- CD into the repository

- Install requirements: `pip install -r requirements.txt`

- Ensure you have set the following environment variables:
    - 'DATABASE_URL'
    - 'EMAIL_ADDRESS
    - 'EMAIL_PASSWORD'
    - 'SECRET_KEY' (arbitrary string)
    - 'DATABASE_URL'
    - 'EMAIL_ADDRESS'
    - 'EMAIL_PASSWORD'
    - 'SECRET_KEY'
    - 'SOCIAL_AUTH_GITHUB_KEY'
    - 'SOCIAL_AUTH_GITHUB_SECRET'
    - 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'
    - 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'
    - 'SOCIAL_AUTH_TWITTER_KEY'
    - 'SOCIAL_AUTH_TWITTER_SECRET'
    - 'STRIPE_PUBLISHABLE'
    - 'STRIPE_SECRET'


- Make migrations: `python3 manage.py makemigrations`

- Migrate: `python3 manage.py migrate`

- Run the server: `python3 manage.py runserver`

```python
requirements.txt

astroid==2.1.0
certifi==2018.11.29
chardet==3.0.4
defusedxml==0.5.0
dj-database-url==0.5.0
Django==1.11.15
django-colorfield==0.1.15
django-forms-bootstrap==3.1.0
django-js-asset==1.1.0
django-tinymce4-lite==1.7.3
gunicorn==19.9.0
idna==2.7
isort==4.3.4
jsmin==2.2.2
lazy-object-proxy==1.3.1
mccabe==0.6.1
oauthlib==3.0.0
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
stripe==2.18.0
sweetify==1.0.3
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
