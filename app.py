from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class Practice(db.Model, UserMixin):
    __tablename__ = 'practice'
    id = db.Column(db.String(500), primary_key=True)
    title = db.Column(db.Text)
    contact = db.Column(db.String(100))
    website_link = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(500))

   

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yhc_db.sqlite3'

db.init_app(app)

# Create tables when the application starts
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    practices = Practice.query.all()
    return render_template('index.html',practices=practices)

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/information')
def information():
    return render_template('information.html')


@app.route('/directory')
def directory():
    practices = Practice.query.all()

    return render_template('directory.html', practices = practices)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=False)
