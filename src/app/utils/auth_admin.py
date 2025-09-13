from functools import wraps
from flask_login import login_required, current_user
from flask import flash, redirect, url_for

def admin_required(funcao_original):
    @wraps(funcao_original)
    @login_required
    def funcao_decorada(*args, **kwargs):
        if current_user.role != "admin":
            flash ("O usuário não tem as permissões necessárias para acessar a página", "warning")
            return redirect(url_for("home.home"))
        return funcao_original(*args, **kwargs)
    return funcao_decorada