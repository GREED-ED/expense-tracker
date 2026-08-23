# Django Expense Tracker

A simple Django web application for tracking personal expenses. Authenticated users can create, view, update, and delete their own expenses. Built with Django's built-in authentication system, a custom user model, and class-based views.

## Features

- User authentication with Django's built-in authentication system
- Custom User model
- Create expenses
- View personal expenses
- Update expenses
- Delete expenses
- Server-side validation
- Users can only access their own expenses
- Django success messages
- SQLite database
- Class-based views

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
expense-tracker/
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
├── expense_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── expenses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       ├── 0001_initial.py
│       └── 0002_expense.py
└── templates/
    ├── base.html
    ├── expenses/
    │   ├── expense_confirm_delete.html
    │   ├── expense_form.html
    │   └── expense_list.html
    └── registration/
        ├── login.html
        └── register.html
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd expense-tracker
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Main Routes

| Route | Purpose |
|---|---|
| `/login/` | User login |
| `/logout/` | User logout |
| `/expenses/` | View personal expenses |
| `/expenses/create/` | Create an expense |
| `/expenses/<id>/edit/` | Edit an expense |
| `/expenses/<id>/delete/` | Delete an expense |
| `/admin/` | Django admin |

## Security

- Expenses are associated with the authenticated user.
- The application filters expenses using the current user, preventing users from accessing or modifying another user's expenses.

## Validation

- Expense title cannot be blank.
- Expense amount must be greater than zero.
- Server-side validation is used for submitted data.

## Configuration Checklist

Make sure the following is set up in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "expenses",
]
```

```python
AUTH_USER_MODEL = "expenses.User"
```

```python
LOGIN_REDIRECT_URL = "/expenses/"
LOGIN_URL = "/login/"
LOGOUT_REDIRECT_URL = "/login/"
```

And in `TEMPLATES`:

```python
"DIRS": [BASE_DIR / "templates"],
```