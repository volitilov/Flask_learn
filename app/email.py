from flask import render_template
from flask_mail import Message, Mail
from app import create_app
from threading import Thread


app = create_app('default')
mail = Mail(app)

def mail_send(msg):
  with app.app_context():
    mail.send(msg)

def send_email(to, subject, template, **kwargs):
  msg = Message(subject, sender='volitilov@gmail.com', recipients=[to])
  msg.body = render_template(template + '.txt', **kwargs)
  msg.html = render_template(template + '.html', **kwargs)
  thr = Thread(target=mail_send, args=[msg,])
  thr.start()
  return thr