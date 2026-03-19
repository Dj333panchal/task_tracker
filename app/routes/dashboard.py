from flask import Blueprint, render_template
from app.models.db import get_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Tasks")
    total_tasks = cursor.fetchone()[0]

    conn.close()

    return render_template('dashboard.html', total_tasks=total_tasks)