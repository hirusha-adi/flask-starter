from flask import render_template
from app.normal import normal

@normal.route('/')
def index():
    return render_template('index.html')
