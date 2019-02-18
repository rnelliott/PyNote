[![Build Status](https://travis-ci.com/davedodea/PyNote.svg?branch=master)](https://travis-ci.com/davedodea/PyNote)
# PyNote
This repository contains the code for a modern note-taking application. It is built largely with Python and the Django framework.

## UX
This application is built with a mobile first, responsive design in mind.

#### User stories

#### New user
- As a first time user, I should: 
    - see a homepage with a header section describing the application.
    - see links to either login or register.

#### Unregistered user
- As a unregistered user, I should:
    - with a form to enable me to register a username, email and password for the site.
    - with the choice to register via OAuth providers such as GitHub, Twitter or Google.

#### Registered user
- As a registered user, I should:
    - see a form to enter my username or email and password.
    - see a link to reset my password if I have forgotten it.

#### Logged In
- As a logged in user, I should:
    - see a confirmation that I have logged in successfully.

#### Notes
- if I have created notes before: 
    - see a screen presenting all of my notes in my account, 
- if not:
    - see a message prompting me to create a note, with a link to the form to create one.

#### Navigation - desktop
- on large/desktop screens:
    - see a top navigation bar with links to:
    - main/home page.
    - create:
        - note, link to the form to create a new note.
        - category, link to a page to manage/create categories.
    - username:
        - profile page where I can edit various fields of info on my user:
            - also view my 'user type' i.e. Premium or else see an Upgrade button.
        - logout button

#### Searching
- search field where I can search all of my notes with keywords.
    - this search ability will search the projects table for matches on the title and content fields

#### Side-nav - mobile    
- see a collapsible side-navigation menu with the following links:
    - main/home page.
    - create a note.
    - search notes field.
    - dropdown menus for both notes and categories.
    - settings/profile.
    - logout button.
- on mobile devices all my navigation is through the side-navigation menu.

#### Creating
- As a user who wants to create a note:
    - If I do not have any categories stored:
        - I should be redirected to the category page to create one.
    - If I do, I should see a form page with the following fields for the note:
        - Name or title.
        - Content - using a rich text [WYSIWYG Editor](https://en.wikipedia.org/wiki/WYSIWYG)so that I can format my note with various text editing options.
        - Category - select a category for the note, only categories which I own should list.

- As a user who has more than 5 notes stored, I should be directed to upgrade.

#### Upgrading/Stripe
- As a user who wants to upgrade I should see a products page listing the premium plan. 
    - If I have already upgraded, I should be directed to the profile page where my 'Premium' badge is displayed.
    - If I have not already upgraded, I should be taken to the products page which will show me:
        -The page should show me:
            - plan details.
            - price of the plan per month.
            - quantity of months which I would like to purchase.
        - After choosing how many months to pay for I should be directed to a payment form which should include:
            - My customer details i.e. name and address.
            - Payment details i.e. credit card form.
        - When my payment was processed, I should be directed to my profile page with an alert informing me that my payment was successful and my user type badge should now say 'Premium'.
            - I am now also able to create more then 5 notes.

#### Editing
- As a logged in user who wants to edit a note:
    - I should click on it's title/name form either the home page or from the dropdown side-nav. 
    - This should direct me to a page with a from where I can edit any existing field of the form.


## Testing, validation and styling
#### Testing
- The site was tested on all modern desktop and mobile browsers to ensure cross compatibility and functionality.
- The site was tested to be responsive and to ensure it would be correctly displayed across mobile devices.
- I ensured that each one of the user stories were thoroughly tested to be functional without errors.

#### Validation
- My HTML, CSS an Javascript were all validated successfully with the relevant online tools.


## Features overview
- Full user account system for authorisation and authentication,.
- Social sign-on via OAuth for GitHub, Twitter and Google.
- Users may create, store and organise the notes.
- Categorise user notes.
- Full search via notes and categories.
- Payment plans via Stripe credit card payment processing.

### Features I'd like to implement in future versions
- Sharable notes to public.
- Allow registered users to edit each other's notes.
- Tags for notes.
- Build a decoupled REST API for all the model functions/views to enable other front ends to be used outside of Django's templates

## Challenges
- Overall, I found learning the Django framework to be difficult at times, but with persistance, I began to find my way and I am now quite comfortable with its functionality. The project has taught me an awful lot about not only Django but also Python as a whole.

- I had never implemented a social sign-on/OAuth system before. This was a great learning experience. I had to read over the documentation of the different providers and learn how to implement them with Django's system.

- Stripe payment processing was another large challenge. Learning how to utilise the Stripe API and integrate with Django was difficult at times. However, I would be confident in installing a similar system again.

- Integrating TinyMCE WYSIWYG editor into Django was a tricky process which required extensive reading of the documentation n order to configure properly. However, I believe the rich text editing functionality enabled by having TinyMCE provides the user with a great experience on both dekstop and mobile.


## Technologies Used
- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [jQuery](https://jquery.com/) - for DOM manipulation.
- [Bootstrap](https://getbpptstrap.com) - Bootstrap is used as the primary CSS framework.
- [Django](https://www.djangoproject.com/) - MVT (Mode-View-Template) framework used to build the application. 
- [PostgreSQL](https://www.postgresql.org/) - Relational database store for model data.
- [Heroku](https://www.heroku.com/) - Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Travis-CI](https://travis-ci.com) - Test and deploy code projects.
- [TinyMCE](https://tiny.cloud) - Advanced WYSIWYG HTML Editor.
- [Stripe](https://stripe.com) - A complete payments platform‎.


## Deployment
- A live version of this app is available [here](https://pynote.daveodea.com).

- The Django application and the PostgreSQL database are deployed to separate Heroku instances.

- Testing is triggered via TravisCI upon PR's to the GitHub repository.

- Once TravisCI builds, deployment is carried out on Heroku.

- The process I took was as follows:
    - 


- If you wish to deploy - ensure you have set the following config vars set in Heroku app settings:
```
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
```

## Install locally

This is the process I have tested to enable local development and deployment.
- Clone the repository.

- CD into the repository.

- Activate a virtual environment using `pipenv`.

- Install requirements: `pipenv install`

- Ensure you have set the `above` environment variables: 
    - Suggest to set the variables in a file called `env.py` and follow the format for `each`:
        - `os.environ['DATABASE_URL'] = '...'` etc.

- Make migrations: `python3 manage.py makemigrations`

- Migrate: `python3 manage.py migrate`

- Collect static files: `python3 manage.py collectstatic`

- Create a super user/admin: `python3 manage.py createsuperuser`

- Run the server: `python3 manage.py runserver`

## Credits

### Third-party
- Social buttons for Bootstrap:
   - https://github.com/lipis/bootstrap-social

- Hover CSS:
   - https://github.com/IanLunn/Hover
