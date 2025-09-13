from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from src.app.forms import TarefaForm, DeleteForm, EditForm
from src.app.models import db, Tarefas
from src.app.utils.auth_admin import admin_required

user_route = Blueprint("user", __name__)


@user_route.route("/admin")
@admin_required
def admin():
    return "você está na rota de administrador"

@user_route.route("/gerenciador_tarefas", methods=["GET", "POST"])
@login_required
def gerenciador_de_tarefas():
    tarefas = Tarefas.query.filter_by(usuario_id=current_user.id).all()
    form_deletar = DeleteForm()
    form_editar = EditForm()
    return render_template("gerenciador.html", tarefas=tarefas, form_deletar=form_deletar, form_editar=form_editar)

@user_route.route("/add_tarefas", methods=["GET", "POST"])
@login_required
def add_tarefa():
    form = TarefaForm()
    
    if form.validate_on_submit():
        titulo = form.titulo.data
        descricao = form.descricao.data
    
        tarefa = Tarefas(usuario_id=current_user.id, titulo=titulo, descricao=descricao)
        
        db.session.add(tarefa)
        db.session.commit()
        
        flash ("Tarefa adicionada com sucesso", "success")
        return redirect(url_for("user.gerenciador_de_tarefas"))

    return render_template("form_tarefas.html", form=form, action="add_tarefas")

@user_route.route("/<int:id>/deletar", methods=["POST"])
@login_required
def deletar(id):
    try:
        tarefa = Tarefas.query.get(int(id))
    except Exception:
        flash ("Usuário não encontrado.", "danger")
        return redirect(url_for("user.gerenciador_de_tarefas"))
    
    form = DeleteForm()
    
    if form.validate_on_submit():
        db.session.delete(tarefa)
        db.session.commit()
        flash ("Tarefa deletada", "warning")
        
    return redirect(url_for("user.gerenciador_de_tarefas"))

@user_route.route("/<int:id>/editar", methods=["GET", "POST"])
@login_required
def editar(id):
    form = TarefaForm()
    
    if form.validate_on_submit():
        tarefa = Tarefas.query.get(int(id))
        
        
        tarefa.titulo = form.titulo.data
        tarefa.descricao = form.descricao.data
        db.session.commit()
        
        flash ("Tarefa atualizada com sucesso.", "success")
        return redirect(url_for("user.gerenciador_de_tarefas"))    
    
    return render_template("form_tarefas.html", form=form, action=f"{id}/editar")