# Django Expense Tracker

A simple personal expense tracker built with Django.

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
├── expense_tracker/
├── expenses/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
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