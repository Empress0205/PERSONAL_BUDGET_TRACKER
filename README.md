# Personal Budget Tracker

A Django web app for tracking personal income and expenses. Users register, log in, record income and expenses, see their balance on a dashboard, browse their history and export transactions to CSV.

## Features

- User registration and login
- Add income and expenses (expenses are blocked if they exceed the available balance)
- Dashboard with current balance and a spending recommendation
- Transaction history
- CSV export

## Stack

Python · Django 5.1 · SQLite · HTML/CSS templates

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key — set a long random value outside local development | development-only key |
| `DJANGO_DEBUG` | `True` or `False` | `True` |
