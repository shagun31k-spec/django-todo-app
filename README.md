# Django Todo App

A simple Todo application built using Django.

This project allows users to add tasks, mark them as complete, edit tasks, and delete tasks.

## Features

- Add new tasks
- View all tasks
- Mark tasks as complete
- Edit existing tasks
- Delete tasks
- Shows the number of remaining tasks
- Simple and colorful user interface

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite

## Project Structure

```text
myproject/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── todo/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    └── templates/
        └── todo/
            ├── home.html
            └── edit.html
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd django-todo-app
```

### 3. Create a virtual environment

```bash
python3 -m venv env
```

### 4. Activate the virtual environment

On macOS/Linux:

```bash
source env/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the Django development server

```bash
python manage.py runserver
```

### 8. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## How It Works

The `Task` model stores each Todo item in the SQLite database.

Each task contains:

- Task title
- Completion status
- Creation time

Django views handle actions such as adding, editing, completing, and deleting tasks.

The HTML templates display the tasks and provide the user interface.

## Future Improvements

Some features that can be added in the future:

- User login and registration
- Due dates for tasks
- Task priorities
- Categories
- Search and filtering
- Dark mode
- Clear completed tasks
- Responsive mobile design

## Author

Created as a beginner Django project to learn the basics of web development using Django.
