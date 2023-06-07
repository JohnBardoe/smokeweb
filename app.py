import flask
import json

import smtplib
from email.mime.text import MIMEText

app = flask.Flask(__name__)
send_to = 'denis@denisco.pro'


def send_email(to, message):
    msg = MIMEText(message)
    msg['Subject'] = 'Registration'
    msg['From'] = 'rega@localhost'
    msg['To'] = to

    s = smtplib.SMTP('localhost')
    s.sendmail('rega@localhost', [to], msg.as_string())
    s.quit()

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/submit')
def submit():
    form = flask.request.form
    name = form['name'] + ' ' + form['surname']
    with open(name, 'w') as f:
        f.write(json.dumps(form))
    send_email(send_to, json.dumps(form))


if __name__ == '__main__':
    app.run(port=5000)
