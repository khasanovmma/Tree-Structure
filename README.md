# Django Project

![Django Logo](https://www.djangoproject.com/s/img/logos/django-logo-negative.png)

## About Project

Create a web page that will display a tree structure of departments
with a list of employees

## Installation

1.  Clone the Repository
    `git clone https://github.com/khasanovmma/Tree-Structure.git

    cd Tree-Structure`

2.  Setup Virtual Environment
    `python -m venv venv
    source venv/bin/activate # For Linux/macOS

    venv\Scripts\activate # For Windows`

3.  Install Dependencies
    `pip install -r requirements/dev.txt`

4. Implement in root `.env` file:
    Example: `.env.example`

4.  Run Migrations
    `python manage.py migrate`

5. Populate db with fake data:
    `python manage.py generate_fake_data`

6.  Start the Development Server
    `python manage.py runserver`

7.  Access the Application Open your browser and go to `http://localhost:8000`

## Configuration

- Settings: Adjust settings in the `settings.py` file to suit your needs.
- Database: Configure database settings in the `settings.py` file.
- Static and Media Files: Configure paths and settings for handling static and media files.

## Support

For any queries or support, contact [khasanovmma010@gmail.com].
