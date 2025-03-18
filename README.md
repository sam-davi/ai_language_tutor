# AI Language Tutor

A Django project for language learning with AI support.

## Getting started

1. Clone the repository and navigate to the project directory.
    * If using a postgres database connection, clone the `aws-postgres` branch instead of `master`.
2. Set up the virtual environment and install the dependencies with `uv sync`
3. Create a `.env` file or rename the `.env.example` file and add the following variables:
	* `SECRET_KEY`: a secret key for Django (you can generate one with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
	* `DEBUG`: a boolean value indicating whether to run the project in debug mode (e.g. `True`)
    * `OPENROUTER_BASE_URL`: the base URL for the OpenRouter API `"https://openrouter.ai/api/v1"`
	* `OPENROUTER_API_KEY`: your OpenRouter API key
    * `DB_NAME`: the name of the Postgres database
    * `DB_USER`: the username for the Postgres database
    * `DB_PASSWORD`: the password for the Postgres database
    * `DB_HOST`: the host connection for the Postgres database
    * `DB_PORT`: the port for the Postgres database
4. Run `python manage.py migrate` to create the database tables.
5. Run `python manage.py runserver` to start the development server.
6. Open a web browser and navigate to `http://localhost:8000/` to see the project in action.

## Setting up allauth social logins

1. Create a new superuser with the command `python manage.py createsuperuser` or `uv run manage.py createsuperuser`
2. Login to the Django admin page at `http://localhost:8000/admin/`
3. Add a new social application at `http://localhost:8000/admin/socialaccount/socialapp/add/` completing the following fields:
    * `Provider` (add any additional providers you want to support to settings.INSTALLED_APPS in `settings.py`)
    * `Name`
    * `Client ID`
    * `Scecret key`

