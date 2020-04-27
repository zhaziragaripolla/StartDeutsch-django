# StartDeutsch-django
This project provides Start Deutsch REST API for iOS Client. 
```json
{
    "users": "https://localhost/api/v1/users/",
    "courses": "https://localhost/api/v1/courses/",
    "tests": "https://localhost/api/v1/tests/",
    "listening-questions": "https://localhost/api/v1/listening-questions/",
    "reading-questions": "https://localhost/api/v1/reading-questions/",
    "letters": "https://localhost/api/v1/letters/",
    "forms": "https://localhost/api/v1/forms/",
    "words": "https://localhost/api/v1/words/",
    "cards": "https://localhost/api/v1/cards/"
}
```
## Installation
<ol>
<li>Clone this repository.<br><code>git clone git@github.com:zhaziragaripolla/StartDeutsch-django.git </code>
<li>Install virtual environment. <br> <code>pip install virtualenv</code>
<li>Create virtual environment. <br> <code>virtualenv -p python3 .</code>
<li>Activate virtual environment.<br> <code>source bin/activate</code>
<li>Install project requirements.<br> <code>pip install -r requirements.txt</code>
</ol>

## Usage
NOTE: For using this project, the <strong>SECRET_KEY, DATABASE_URL</strong> should be known. Create settings.ini file with variables.
<ol>
<li>Run migrations to database. 
  <ul>
    <li><code> python manage.py makemigrations </code>
    <li><code> python manage.py migrate </code>
  </ul>
<li>Run server <code> python manage.py runserver </code>
<li>In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/
</ol>

## REST API

NOTE: API is protected by OAuth2.0 from unauthorized access. To utilize API, your application should be in the list of registered applications. Details [here](https://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html).
<ul>
<li> Get token from endpoint <code>/oauth2/token</code> using your <strong>SECRET ID and SECRET KEY</strong><br>
Successfull response looks like this: <br>

```json
{
    "access_token": "PtK2oFO7sTGEWh7bGwRHkwi4uhHdwY",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read"
}
```
<li>Use obtained Bearer token to make API requests.
</ul>
