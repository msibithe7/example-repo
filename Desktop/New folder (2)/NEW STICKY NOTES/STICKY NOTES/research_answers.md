
# Research Answers

## 1. How HTTP Applications Preserve State (Session Management & Authentication)

HTTP is a stateless protocol, meaning each request from a client to a server is independent and does not retain user-specific data between requests. To preserve the state of an application, especially during authentication and user sessions, web frameworks like Django implement **session management** using the following techniques:

### a. Sessions
Django uses session middleware to store session data either in cookies, a database, or cached storage. Each session has a unique ID stored in a cookie on the user’s browser. On each request, Django checks this session ID and loads the associated session data from the server.

```python
# Example: Storing data in a session
request.session['user_id'] = user.id
```

### b. Authentication Middleware
Django includes built-in authentication middleware to manage logged-in users. After logging in, Django stores the user's ID in the session and populates `request.user` with the authenticated user object on each request.

```python
from django.contrib.auth import authenticate, login

user = authenticate(username='themba', password='password123')
if user is not None:
    login(request, user)
```

These tools combined ensure that users stay logged in across multiple request-response cycles securely.

---

## 2. Django Database Migrations to MariaDB

### a. Install MariaDB dependencies
First, install the database driver for MariaDB (mysqlclient):

```bash
pip install mysqlclient
```

Ensure MariaDB server is installed and running.

### b. Update `settings.py`

In the `DATABASES` section of your Django `settings.py`, update the configuration to connect to MariaDB:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sticky_notes_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### c. Run migrations

After connecting Django to MariaDB, run the following commands to apply your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### d. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

MariaDB will now store your application's data instead of SQLite, making it ready for scalable, server-based deployment.
