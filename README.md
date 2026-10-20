# Study Buddy

#### Video Demo: https://youtu.be/4rzt57wrSa4

#### Description:

Study Buddy is a student productivity tracker built using Python, Flask, SQLite, HTML, and CSS. I developed it as my CS50x final project to apply the programming and web development concepts I learned during the course.

The purpose of Study Buddy is to help students organize their tasks and keep track of their progress through a simple web application. Students can add tasks, view their tasks, mark tasks as completed, undo completion, and delete tasks. The dashboard also displays task counts to give users an overview of their progress. Task information is stored in an SQLite database, allowing it to persist when the application is restarted.

I chose this project because managing academic tasks is a common challenge for students. I wanted to create something practical that I could use and potentially improve in the future. Rather than building only a static webpage, I wanted to understand how a web application connects its interface, Python logic, and database.

#### Files and Implementation:

**app.py**

This is the main Python file. It contains the Flask application and the routes that handle requests from the browser. Flask connects the webpage to the Python code that manages the application's functionality. The application handles task-related actions, including adding, completing, undoing, and deleting tasks. It also works with the SQLite database to store and retrieve task information.

**templates/index.html**

This file contains the HTML template for the main page. It defines the structure of the interface, including the areas where tasks and dashboard information are displayed. The template works with the Flask application to present the information to the user.

**static/style.css**

This file contains the CSS used to style the application. I chose a mauve and lilac colour palette to make the interface feel welcoming and visually consistent. Separating the styling from the HTML also makes the design easier to maintain and modify.

**.gitignore**

This file specifies files and directories that should not be included in version control, such as the virtual environment, Python cache files, local database files, and environment configuration files. This keeps unnecessary local files out of the GitHub repository.

#### Technologies Used:

I used Python for the application logic and Flask as the web framework. HTML provides the structure of the webpage, while CSS controls its appearance. SQLite stores task data without requiring a separate database server. I also used Git and GitHub to track changes and maintain an online repository of my project.

#### Design Decisions and Challenges:

I chose Flask because it allowed me to build a web application using Python while learning how routes, functions, and HTML templates work together. SQLite was suitable for this project because the application needed persistent storage without the complexity of setting up a separate database server.

During development, I learned how to connect a webpage to backend functionality, handle user actions, store information in a database, and organize code across different files. I also tested the task-management features to check that tasks could be added, completed, restored, and deleted as expected.

One of the most valuable parts of this project was learning how the different components work together. Building the application helped me move beyond writing individual programming exercises and start developing a complete, working application.

#### Acknowledgments:

I used CS50x as part of my learning journey and ChatGPT as a learning and development aid while building this project. I used this assistance to understand concepts and work through implementation challenges, and I tested the application's functionality during development.
