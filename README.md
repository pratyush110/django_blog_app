# Blog Web Application
## Using Django Framework for development
## live version of app is deployed using heroku at:
https://hellraiserblog.herokuapp.com/
### Small blog app to showcase django knowledge
#### has following features:

- user registration, login and logout
- user profile, profile picture update 
- password reset through email verification
- post create, update and delete


### To run the app in linux environment

- create virtual environment

  ` python3 -m venv env `

- activate the env

  ` source env/bin/activate `

- install the dependencies

  ` pip install -r requirements `

- run the blog app at 127.0.0:8000
  
  `python manage.py runserver`

**This app is using AWS S3 for storing profile pictures**

[to use the local file system comment out the last two lines](./django_project/settings.py)
