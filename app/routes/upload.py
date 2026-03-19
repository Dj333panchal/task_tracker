from flask import Blueprint, request, redirect, url_for
import pandas as pd
from app.models.db import get_connection

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file:
        df = pd.read_excel(file)

        conn = get_connection()
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO Tasks (title, description, assigned_to) VALUES (?, ?, ?)",
                (row['title'], row['description'], row['assigned_to'])
            )

        conn.commit()
        conn.close()

    return redirect(url_for('dashboard.dashboard'))