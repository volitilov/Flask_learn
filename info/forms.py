from flask_wtf import FlaskForm

# form fields
from wtforms import (
  TextField,       # текстовое поле
  TextAreaField,   # многострочное текстовое поле
  PasswordField,   # поле для пароля
  HiddenField,     # скрытое текстовое поле
  DateField,       # поле принимающее дату
  DateTimeField,   # поле принимающее время
  IntegerField,    # целочисленное значение
  DecimalField,    # десятичное число
  FloatField,      # вещественное значение
  BooleanField,    # флажок
  RadioField,      # radio
  SelectField,     # раскрывающийся список вариантов
  
  SelectMultipleField,  # раскрывающийся список вариантов с 
					            	# возможностью выбирать сразу несколько
  
  FileField,       # поле выгрузки файлов
  SubmitField,     # кнопка отправки формы
  FormField,       # встроенная форма как поле вмещающее форму
  FieldList        # список полей указанного типа
)

# form validators
from wtforms.validators import (
  Email,          # проверяет адрес электроной почты 
  EqualTo,        # сравнивает значение двух полей
  IPAddress,      # проверяет сетевой адрес IPv4
  Length,         # проверяет длину ведённой строки
  
  NumberRange,    # проверяет вхождение введённого значения в 
				          # определённый диапазон
  
  Optional,       # допускает отсутствие введённых данных, 
				          # пропускает дополнительные валидаторы

  Required,       # требует наличие введённого значения в поле
  Regexp,         # проверяет на соответствие регулярному выражению
  URL,            # проверяет адрес URL
  
  AnyOf,          # проверяет введённое значение на совпадение с 
				          # любым из списка значением
  
  NoneOf          # проверяет введённое значение на отсутствие 
				          # совпадения с любым из списка недопустимых значений
)


class NameForm(FlaskForm):
  email = TextField('text field', validators=[Required(), Email()])