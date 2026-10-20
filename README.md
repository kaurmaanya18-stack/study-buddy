# Study Buddy

#### Video Demo: https://youtu.be/4rzt57wrSa4

## Description

Study Buddy is a student productivity tracker built using Python, Flask, SQLite, HTML, and CSS. I developed it as my CS50x final project to apply the programming, database, and web development concepts I learned during the course.

The application helps students organize academic tasks and monitor their progress. Users can add tasks, optionally assign due dates, view their task list, mark tasks as completed, undo completion, and delete tasks. A dashboard displays the total number of tasks, completed tasks, and pending tasks.

Task information is stored in an SQLite database, allowing it to persist when the application is restarted. The interface uses a mauve and lilac colour palette.

I chose this project because organizing academic work is a practical challenge for students. I wanted to build something useful rather than only a static webpage and learn how a browser interface, Python backend, and database work together.

## Installation and Usage

1. Install Python.
2. Open a terminal in the project directory containing `app.py`.
3. Create a virtual environment with `python -m venv .venv`.
4. Activate the environment:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Linux/macOS: `source .venv/bin/activate`
5. Install Flask with `python -m pip install Flask`.
6. Start the application with `python app.py`.
7. Open `http://127.0.0.1:5000` in a browser.

The application initializes the database table if it does not already exist.

## Files and Implementation

### `app.py`

This file contains the Flask application and its routes.

- `get_db_connection()` connects to the SQLite database and allows database columns to be accessed by name.
- `initialize_db()` creates the tasks table if it does not already exist.
- The `/` route retrieves tasks and calculates dashboard totals.
- The `/add` route processes new tasks and their optional due dates.
- The `/complete/<int:task_id>` route toggles a task's completion status.
- The `/delete/<int:task_id>` route deletes a task.

Parameterized SQL queries are used when handling task input.

### `templates/index.html`

This file defines the main page using HTML and Jinja template syntax. It displays the dashboard, task form, and task list. A loop displays each task, while conditional statements handle empty lists and task statuses. Flask's `url_for()` function generates links to routes and static files.

### `static/style.css`

This file controls the application's colours, typography, spacing, cards, forms, buttons, and responsive layout. I chose mauve and lilac shades to create a calm and consistent interface.

### `tasks.db`

This SQLite database stores task records, including their titles, optional due dates, and completion statuses. The application initializes the table when needed.

### `.gitignore`

This file specifies local files and directories that should not be tracked by Git, such as the virtual environment and Python cache files.

## Technologies Used

- **Python:** Application logic.
- **Flask:** Web framework.
- **SQLite:** Persistent task storage.
- **HTML:** Page structure.
- **CSS:** Styling and responsive layout.
- **Jinja:** Dynamic HTML rendering.
- **Git and GitHub:** Version control and source-code hosting.

## Design Decisions and Challenges

I chose Flask because it allowed me to build a web application using Python and learn how routes, templates, and browser requests work together. SQLite provided persistent storage without requiring a separate database server.

During development, I learned how to connect a form to backend logic, save information in a database, update task completion status, delete records, and display dynamic dashboard counts. I tested adding, completing, undoing, and deleting tasks, as well as checking that saved tasks remained available after reopening the application.

Building Study Buddy helped me move beyond individual programming exercises and gain experience combining several technologies into a working application. Future improvements could include task filtering and editing existing tasks.

## Acknowledgments

I used CS50x course materials during my learning journey and ChatGPT as a learning and development aid while working through programming concepts and implementation challenges. I tested the application's functionality during development.
