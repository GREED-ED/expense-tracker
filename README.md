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

## Steps to Test the Application

1. Visit `http://127.0.0.1:8000/` — you should be redirected to `/login/` because the expense pages require authentication.

2. Click **Register** and create a new account. After successful registration, you should be logged in automatically and redirected to the **My Expenses** page.

3. On the **My Expenses** page, click **Add Expense** and fill in a title, amount, category, and date. Select a category from the dropdown and submit the form. You should see a success message and the new expense should appear in the table.

4. Try submitting an expense with an empty title or a negative/zero amount. The form should reject the submission and display a validation error.

5. Click **Edit** on one of your expenses, change a value, and save. The updated value should be reflected in the expense list and a success message should be displayed.

6. Click **Delete** on an expense, confirm the deletion, and verify that the expense is removed from the list. A success message should be displayed.

7. Use the filter form at the top of the list page to filter expenses by **category**, **start date**, and/or **end date**. Verify that only matching expenses are displayed. Check that the **Total (current filter)** and **Total for the current month** figures update according to the displayed/filter criteria.

8. Use the **Clear** option to remove the active filters and verify that all of the logged-in user's expenses are displayed again.

9. Log out, then try visiting `/expenses/` directly. You should be redirected back to the login page.

10. Log in as a different user and confirm that you cannot see the first user's expenses. Try manually guessing an expense ID in the edit or delete URL, such as `/expenses/4/edit/` or `/expenses/4/delete/`. The application should return a **404** because users can only access their own expenses.

11. Verify the monthly total by creating expenses with dates in the current month and another month. The **Total for the current month** should only include expenses from the current month.

12. Verify the registration flow by logging out and creating another account through **Register**. Confirm that the new user starts with their own empty expense list and cannot access another user's expenses.


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