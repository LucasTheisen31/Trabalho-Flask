from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    name = StringField('Usuário', validators=[DataRequired(), Length(min=4, max=100)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Login')
    
class RegisterForm(FlaskForm):
    name = StringField('Usuário', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=40)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')
    
class TaskForm(FlaskForm):
    task_description = StringField('Descrição da Tarefa', validators=[DataRequired(), Length(min=4, max=100)])
    submit = SubmitField('Adicionar Tarefa')