from flask import render_template
from flask import render_template
from app import app, db  # Adjust the import statement
from app.models import *  # Adjust the import statement


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
