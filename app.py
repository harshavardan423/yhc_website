from flask import Flask, render_template,request,redirect,url_for,send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary
from flask_login import UserMixin
import os
import base64
from io import BytesIO


port = int(os.environ.get("PORT", 5000))



db = SQLAlchemy()

class Practice(db.Model):
    __tablename__ = 'practice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20))
    website_link = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.LargeBinary)
   

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yhc_db.sqlite3'

db.init_app(app)

# Create tables when the application starts
with app.app_context():
    db.create_all()

#    # Storing image data
#     with open("C:/Users/H2/Documents/GitHub/yhc_website/static/imgs/FB-DENTAL.png", "rb") as f:
#         image_data = f.read()

#     # Encode the image data to base64
#     encoded_image = base64.b64encode(image_data)

#     practice1 = Practice(
#         title="FB Dental",
#         contact="(07) 5666 7258",
#         website_link="https://www.fbdental.au/",
#         description="Discover outstanding and affordable dental care at FB Dental, conveniently located on the ground floor of Yarrabilba Health City. Our commitment to patient-centred care is reflected in our state-of-the-art clinic, where we seamlessly integrate cutting-edge technology to provide a complete digital dentistry experience. Our welcoming team ensures a relaxed experience with personalised treatments in a relaxed environment. Come and witness the excellence firsthand at FB Dental Yarrabilba, and embark on your journey to optimal oral health!",
#         image=encoded_image  # Keep it as bytes
#     )

#     db.session.add(practice1)
#     db.session.commit()



@app.route('/add_practice', methods=['GET', 'POST'])
def add_practice():
    if request.method == 'POST':
        title = request.form['title']
        contact = request.form['contact']
        website_link = request.form['website_link']
        description = request.form['description']
        image = request.files['image'].read() if 'image' in request.files else None

        new_practice = Practice(title=title, contact=contact, website_link=website_link,
                                description=description, image=image)
        db.session.add(new_practice)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_practice.html')


@app.route('/get_image/<int:image_id>')
def get_image(image_id):
    practice = Practice.query.get_or_404(image_id)
    if practice.image:
        return send_file(BytesIO(practice.image), mimetype='image/jpeg')
    else:
        # Return a placeholder image or handle the situation appropriately
        return send_file('path_to_placeholder_image', mimetype='image/jpeg')


@app.route('/practice_details/<int:practice_id>')
def practice_details(practice_id):
    # Assuming you have a Practice model with details such as title, description, etc.
    practice = Practice.query.get_or_404(practice_id)
    return render_template('practice_details.html', practice=practice)
    

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
    app.run(host='0.0.0.0', port=port,debug=True)