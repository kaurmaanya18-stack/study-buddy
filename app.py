import sqlite3
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store the database in the same folder as app.py.
DATABASE = Path(__file__).resolve().parent / "tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


# Create the tasks table if it doesn't already exist.
def initialize_db():
    connection = get_db_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    connection.commit()
    connection.close()


@app.route("/")
def index():
    connection = get_db_connection()
    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY completed ASC, id DESC"
    ).fetchall()

    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed
    connection.close()

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    due_date = request.form.get("due_date", "").strip()

    if title:
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO tasks (title, due_date) VALUES (?, ?)",
            (title, due_date or None)
        )
        connection.commit()
        connection.close()

    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    connection = get_db_connection()
    connection.execute(
        "UPDATE tasks SET completed = 1 - completed WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_db_connection()
    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


initialize_db()

if __name__ == "__main__":
    app.run(debug=True)
