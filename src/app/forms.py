from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class CadastroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(message="O nome não pode estar vazio.")])
    email = StringField("E-mail", validators=[DataRequired(message="O e-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                               Length(min=8, message="A senha deve ter no mínimo 8 caracteres.")])
    conf_senha = PasswordField("Confirmar Senha", validators=[DataRequired(message="Senha vazia."),
                                            Length(min=8, message="A senha deve ter no mínimo 8 caracteres."),
                                            EqualTo("senha", message="As senhas não coincidem.")])
    cadastrar = SubmitField("Cadastrar")                                                    
    
class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(message="O e-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                               Length(min=8, message="A senha deve ter no mínimo 8 caracteres.")])
    login = SubmitField("Login")
    
class TarefaForm(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired(message="O título deve ser escolhido.")])
    descricao = TextAreaField("Descrição", validators=[DataRequired(message="Digite pelo menos alguma coisa na descrição.")])
    salvar = SubmitField("Salvar")
    
class DeleteForm(FlaskForm):
    deletar = SubmitField("Deletar")
    
class EditForm(FlaskForm):
    editar = SubmitField("Editar")