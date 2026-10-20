# Study Buddy

#### Video Demo: https://youtu.be/4rzt57wrSa4

#### Description

Study Buddy is a student productivity tracker built using Python, Flask, SQLite, HTML, and CSS. I developed it as my CS50x final project to apply the programming, database, and web development concepts I learned during the course.

The purpose of Study Buddy is to help students organize academic tasks and monitor their progress through a simple web application. Users can add tasks, optionally assign due dates, view their task list, mark tasks as completed, undo completion, and delete tasks. The dashboard displays the total number of tasks, completed tasks, and pending tasks.

Task information is stored in an SQLite database, allowing tasks to persist when the application is restarted. The interface uses a mauve and lilac colour palette, with separate sections for the dashboard, task form, and task list.

I chose this project because organizing academic work is a practical challenge for students. I wanted to build something useful rather than only a static webpage. The project helped me understand how a browser interface, Python backend, and database work together in a functioning web application.

#### Installation and Usage

Study Buddy runs locally using Python and Flask. To run it, Python must be installed on the computer.

1. Open a terminal in the project directory containing `app.py`.
2. Create a virtual environment using `python -m venv .venv`.
3. Activate the virtual environment. On Windows PowerShell, run `.venv\Scripts\Activate.ps1`. On Linux or macOS, run `source .venv/bin/activate`.
4. Install Flask using `python -m pip install Flask`.
5. Start the application using `python app.py`.
6. Open `http://127.0.0.1:5000` in a web browser.

The application initializes the database table when it starts if the table does not already exist. The SQLite database is stored in the project directory as `tasks.db`. Existing database contents are retained when the application is restarted.

#### Files and Implementation

**`app.py`**

This is the main Python file and contains the Flask application. It defines the routes that connect browser requests to application functionality.

The `get_db_connection()` function creates a connection to the SQLite database and configures database rows so their columns can be accessed by name. The `initialize_db()` function creates the `tasks` table if it does not already exist. The table stores each task's ID, title, optional due date, and completion status.

The `/` route retrieves tasks from the database and calculates the total, completed, and pending task counts before passing the information to the HTML template.

The `/add` route accepts a POST request from the task form, reads the task title and optional due date, and inserts the task into the database. Parameterized SQL queries are used to handle user input safely.

The `/complete/<int:task_id>` route toggles a task's completion status, allowing users to complete a task or undo completion. The `/delete/<int:task_id>` route deletes a task using its ID. After these actions, the application redirects the user to the main page.

**`templates/index.html`**

This file defines the structure of the main page using HTML and Jinja template syntax supported by Flask.

It displays the dashboard totals, provides a form for adding tasks, and lists saved tasks. Conditional statements display either the task list or a message when no tasks exist. A loop generates the interface for each task, including its title, optional due date, status, and action buttons.

The template uses `url_for()` to generate URLs for Flask routes and the CSS file. This connects the page's forms and styling to the application without manually hardcoding those URLs.

**`static/style.css`**

This file controls the appearance of Study Buddy. It defines the colour palette, typography, spacing, cards, forms, buttons, task list, and hover effects. CSS variables make it easier to maintain consistent colours throughout the interface.

I chose mauve and lilac shades to create a calm and welcoming design. A responsive CSS media query changes the dashboard layout on smaller screens and stacks task details and actions vertically to make the application easier to use on mobile devices.

**`tasks.db`**

This is the SQLite database used to store task information. The application creates the database table when it starts if the table does not already exist. Task records are stored in the database so they remain available after the page is refreshed or the application is restarted.

**`.gitignore`**

This file specifies local files and directories that should not be tracked by Git, such as the Python virtual environment, cache files, and local configuration files. This helps keep the repository focused on the project source code.

#### Technologies Used

- **Python:** Application logic and task-management operations.
- **Flask:** Web framework connecting browser requests to Python functions.
- **SQLite:** Database for persistent task storage.
- **HTML:** Structure of the application interface.
- **CSS:** Styling and responsive layout.
- **Jinja:** Dynamic rendering of task data and dashboard values.
- **Git and GitHub:** Version control and source-code hosting.

#### Design Decisions and Challenges

I chose Flask because it allowed me to build a web application with Python and understand how routes, templates, and user requests work together. SQLite was appropriate for this project because it provided persistent storage without requiring a separate database server.

One of the main learning experiences was connecting the task form to backend logic and storing submitted information in a database. I also worked on displaying dynamic task counts, updating completion status, deleting records, and keeping the interface synchronized with stored data.

Organizing the application into a Python file, an HTML template, a stylesheet, and a database helped me understand the purpose of separating application logic, page structure, visual presentation, and data storage.

I tested the main task-management workflow by adding tasks, marking them complete, undoing completion, deleting tasks, and checking whether saved tasks remained available after reopening the application.

Building Study Buddy helped me move beyond individual programming exercises and gain experience putting multiple technologies together in a complete application. It also gave me a foundation for future improvements, such as task filtering, editing existing tasks, and additional productivity features.

#### Acknowledgments

I used CS50x course materials as part of my learning journey and ChatGPT as a learning and development aid while working through programming concepts and implementation challenges. I reviewed and tested the application's functionality during development.