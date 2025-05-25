# Remind-Me-Later

Remind-Me-Later is a simple web API built using Django REST Framework. It allows users to create scheduled reminders that can be delivered via email or SMS (future support for more delivery types is planned). This project provides an API endpoint to save reminders with a message, date, time, and method of notification.

---

## Requirements

To run this project, you need the following installed:

- Python 3.10 or above
- pip (Python package manager)
- Virtual environment (optional but recommended)
- Git
- Django
- Django REST Framework

You can install the required packages using:

pip install django djangorestframework

## Project Setup

1. Clone the repository:

git clone https://github.com/your-username/remind-me-later.git

cd remind-me-later

2. Create and activate a virtual environment:

python -m venv env

.\env\Scripts\activate     ( For Windows PowerShell)

3. Install Dependencies:

pip install -r requirements.txt

4. Run Migrations:

python manage.py makemigrations
python manage.py migrate

5. Start the development server:

python manage.py runserver


## HOW to Use the API

You can test the API using VS Code's Extension Postman.

* Request Type
Method: POST

URL: http://127.0.0.1:8000/reminders/create/

Headers:

Content-Type: application/json

Sample Input (JSON Body)

{
  "message": "Meeting with team",
  "date": "2025-05-27",
  "time": "14:00:00",
  "reminder_type": "email"
}

Expected Output (Response)

{
  "id": 1,
  "date": "2025-05-27",
  "time": "14:00:00",
  "message": "Meeting with team",
  "reminder_type": "email",
  "created_at": "2025-05-25T10:44:22.077429Z"
}


