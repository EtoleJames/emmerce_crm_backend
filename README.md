[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/EtoleJames/emmerce_crm_backend/badge.svg?branch=develop)](https://coveralls.io/github/EtoleJames/emmerce_crm_backend?branch=develop)

# Emmerce Mini CRM

## Project Description

**Emmerce Mini CRM** is a comprehensive backend application built with Django and Django REST Framework to manage leads, contacts, notes, and reminders effectively. It is designed to demonstrate best practices in building RESTful APIs, asynchronous task management using Celery with Redis, and secure authentication using JSON Web Tokens (JWT). This project also includes a structured and scalable folder hierarchy to ensure maintainability and extensibility. You can use this swagger link to visit the site. It is hosted in Railway.

[https://emmercecrmbackend-production.up.railway.app/swagger](https://emmercecrmbackend-production.up.railway.app/swagger)

---

## Project Structure

Here’s the detailed project structure:

```plaintext
emmerce_crm_backend/
├── .coveralls.yml           # Configuration for Coveralls
├── .dockerignore            # Docker ignore file
├── .env                     # Environment variables
├── .gitignore               # Git ignore file
├── Dockerfile               # Dockerfile for building the application
├── docker-compose.yaml      # Docker Compose file
├── manage.py                # Django management script
├── Procfile                 # Heroku deployment configuration
├── requirements.txt         # Python dependencies
├── static_files/            # Static files for the application
├── .venv/                   # Virtual environment (optional, local use)
├── emmerce_crm_backend/     # Django project folder
│   ├── __init__.py
│   ├── asgi.py              # ASGI configuration
│   ├── celery.py            # Celery configuration
│   ├── settings/            # Settings folder
│   │   ├── __init__.py
│   │   ├── base.py          # Base settings
│   │   ├── dev.py           # Development settings
│   │   ├── staging.py       # Staging settings
│   │   └── prod.py          # Production settings
│   ├── urls.py              # URL configuration
│   ├── wsgi.py              # WSGI configuration
│   ├── apps/                # Apps folder containing API components
│   │   ├── authentication/  # Authentication app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── contacts/        # Contacts app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── leads/           # Leads app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── notes/           # Notes app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── reminders/       # Reminders app
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
└── README.md                # Project documentation
```

---

## Endpoints

### Authentication (JWT)

- **POST** `/api/register/` - Register a new user.
- **POST** `/api/login/` - Log in an existing user.
- **POST** `/api/logout/` - Log out the current user.
- **POST** `/api/token/` - Obtain an access and refresh token.
- **POST** `/api/token/refresh/` - Refresh an expired access token.

### Leads

- **GET** `/api/leads/` - Retrieve all leads.
- **POST** `/api/leads/` - Create a new lead.
- **GET** `/api/leads/<id>/` - Retrieve a lead by ID.
- **PUT** `/api/leads/<id>/` - Update a lead by ID.
- **PATCH** `/api/leads/<id>/` - Partially update a lead by ID.
- **DELETE** `/api/leads/<id>/` - Delete a lead by ID.

### Contacts

- **GET** `/api/contacts/` - Retrieve all contacts.
- **POST** `/api/contacts/` - Create a new contact.
- **GET** `/api/contacts/<id>/` - Retrieve a contact by ID.
- **PUT** `/api/contacts/<id>/` - Update a contact by ID.
- **PATCH** `/api/contacts/<id>/` - Partially update a contact by ID.
- **DELETE** `/api/contacts/<id>/` - Delete a contact by ID.

### Notes

- **GET** `/api/notes/` - Retrieve all notes.
- **POST** `/api/notes/` - Create a note linked to a lead.
- **GET** `/api/notes/<id>/` - Retrieve a note by ID.
- **PUT** `/api/notes/<id>/` - Update a note by ID.
- **PATCH** `/api/notes/<id>/` - Partially update a note by ID.
- **DELETE** `/api/notes/<id>/` - Delete a note by ID.

### Reminders

- **GET** `/api/reminders/` - Retrieve all reminders.
- **POST** `/api/reminders/` - Create a reminder linked to a lead.
- **GET** `/api/reminders/<id>/` - Retrieve a reminder by ID.
- **PUT** `/api/reminders/<id>/` - Update a reminder by ID.
- **PATCH** `/api/reminders/<id>/` - Partially update a reminder by ID.
- **DELETE** `/api/reminders/<id>/` - Delete a reminder by ID.
- **POST** `/api/reminders/send_reminder/` - Trigger an email reminder asynchronously.

---

## Technologies Used

- **Django**: High-level Python web framework.
- **Django REST Framework**: For building APIs.
- **Celery**: For managing asynchronous tasks.
- **Redis**: Message broker for Celery.
- **PostgreSQL**: Database for storing application data.
- **JWT**: Secure authentication method.

---

## Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- Redis

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/EtoleJames/emmerce_crm_backend.git
   cd emmerce_crm_backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py migrate --settings=emmerce_crm_backend.settings.dev
   ```

4. Start the Redis server:

   ```bash
   redis-server
   ```

5. Start the Celery worker:

   ```bash
   celery -A emmerce_crm_backend worker --loglevel=info
   ```

6. Run the development server:
   ```bash
   python manage.py runserver --settings=emmerce_crm_backend.settings.dev
   ```

---

## Testing

Run the test suite to ensure everything works correctly:

```bash
python manage.py test --settings=emmerce_crm_backend.settings.test
```

---

## Requirements

Some key libraries used in the application include:

- **Celery** (5.4.0): For managing asynchronous tasks.
- **Redis** (5.2.1): Message broker for Celery.
- **Django REST Framework** (3.15.2): For creating APIs.
- **djangorestframework-simplejwt** (5.3.1): For JWT-based authentication.
- **django-celery-beat** (2.7.0): For periodic task scheduling.

For the full list of dependencies, see [requirements.txt](./requirements.txt).

---

## Author

**James Etole**  
📧 Email: [etolejames@gmail.com](mailto:etolejames@gmail.com)
