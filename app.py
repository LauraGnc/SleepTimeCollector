from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Rice123//@localhost/sleep_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kkhouakhlizbjv:e207382b6e0827189bd8eea4bce9708105bf3e33b3f10e988d6952928db4deac@ec2-54-161-150-170.compute-1.amazonaws.com:5432/d6p4qggb8sm21c'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__= 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    sleep_ = db.Column(db.Integer)

    def __init__(self, email_, sleep_):
        self.email_ = email_
        self.sleep_ = sleep_

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        sleep = request.form['sleep_name']

        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, sleep)
            db.session.add(data)
            db.session.commit()
            average_sleep = db.session.query(func.avg(Data.sleep_)).scalar()
            average_sleep = round(average_sleep, 1)
            count = db.session.query(Data.sleep_).count()
            send_email(email, sleep, average_sleep, count)
            print(average_sleep)
            return render_template('success.html')
        else:
            return render_template('index.html', text='The email is already registered with us!')

if __name__ == '__main__':
    app.debug=True
    app.run()
