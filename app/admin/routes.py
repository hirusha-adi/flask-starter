from flask import render_template
from app.admin import admin

@admin.route('/')
def admin_index():
    return render_template('admin_index.html')
