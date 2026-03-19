from flask import Blueprint, request, redirect, url_for
from app.models.db import get_connection

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks/create', methods=['POST'])
def create_task():
    title = request.form['title']
    description = request.form['description']
    assigned_to = request.form['assigned_to']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Tasks (title, description, assigned_to) VALUES (?, ?, ?)",
        (title, description, assigned_to)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('dashboard.dashboard'))