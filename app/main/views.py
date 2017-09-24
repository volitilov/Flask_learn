from flask import (
  render_template, 
  make_response, 
  redirect,
  session,
  url_for,
  flash
)
from . import main
from .forms import TestForm
from .. import db, config
from ..email import send_email
from ..models import Role, User



@main.route('/', methods=['POST', 'GET'])
def index():
  admin = 'volitilov@gmail.com'
  title = 'Home'
  form = TestForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.name.data).first()
    if user is None:
      user = User(username=form.name.data)
      db.session.add(user)
      session['known'] = False
      if admin:
        send_email(admin, 'New user', 'mail/new_user', user=user)
    else:
      session['known'] = True

    session['name'] = form.name.data
    form.name.data = ''
    return redirect(url_for('.index'))
  return render_template('index.html', 
            user=session.get('name'), 
            title=title, 
            form=form,
            known=session.get('known', False))