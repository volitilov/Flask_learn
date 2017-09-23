from flask import render_template
from flask_mail import Message
from app import app, mail
from threading import Thread


def mail_send(msg):
  with app.app_context():
    mail.send(msg)

def send_email(to, subject, template, **kwargs):
  msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                recipients=[to])
  msg.body = render_template(template + '.txt', **kwargs)
  msg.html = render_template(template + '.html', **kwargs)
  thr = Thread(target=mail_send, args=[msg,])
  thr.start()
  return thr