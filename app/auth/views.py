from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import Loginform, RegistrationForm



@auth.before_app_request
def before_request():
  if current_user.is_authenticated \
    and not current_user.confirmed \
    and request.endpoint \
    and request.endpoint[:5] != 'auth.' \
    and request.endpoint != 'static':
      return redirect(url_for('auth.unconfirmed'))



@auth.route('/login', methods=['GET', 'POST'])
def login():
  title = 'Login'
  form = Loginform()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):

      login_user(user, form.remember_me.data)
      # для запоминания аутентифицированного пользователя, она 
      # принимает объект представляющий пользователя и необязательный 
      # логический флаг "запомнить меня", тоже полученный с формой. 
      # Значение False в этом аргументе приводит к закрытию сеанса 
      # пользователя сразу после закрытия окна пользователя, 
      # вследствии чего при следующем посищении приложения ему вновь 
      # придётся пройти процедуру аутентификации. Значение True вызовет 
      # создание cookie с длительным сроком хранения и отправку его 
      # браузеру пользователя, с помощью которого можно будет 
      # востановить прерванный сеанс
      
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('invalid username or password.')
  return render_template('auth/login.html', form=form, title=title)



@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logeed out.')
  return redirect(url_for('main.index'))



@auth.route('/register', methods=['GET', 'POST'])
def register():
  title = 'Registration'
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data,
                password=form.password.data)
    db.session.add(user)
    db.session.commit()
    token = user.generate_confirmation_token()
    send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', 
                    user=user, token=token)
    flash('Письмо для подтверждения регистрации отправленно, на почтовый ящик')
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', form=form, title=title)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
  if current_user.confirmed:
    return redirect(url_for('main.index'))
  if current_user.confirm(token):
    flash('Ваш аккаунт потверждён спосибо!')
  else:
    flash('Ваша ссылка не действительна либо истекло время ссылки.')
  return redirect(url_for('main.index'))



@auth.route('/unconfirmed')
def unconfirmed():
  if current_user.is_anonymous or current_user.confirmed:
    return redirect(url_for('main.index'))
  return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
  token = current_user.generate_confirmation_token()
  send_email(current_user.email, 'Confirm Your account', 'auth/email/confirm', user=current_user, token=token)
  flash('A new confirmation emailhas been sent to you by email.')
  return redirect(url_for('main.index'))