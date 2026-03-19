from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from app.models.db import get_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Users WHERE Username=?", username)
        user = cursor.fetchone()

        if user:
            login_user(user)
            return redirect('/dashboard')

    return render_template('login.html')