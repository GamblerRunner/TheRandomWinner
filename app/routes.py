from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Bienvenido a mi aplicación Flask con SurrealDB!"

@bp.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query = request.form.get('query')
        try:
            result = db(query)
            flash(f"Consulta exitosa: {result}", 'success')
        except Exception as e:
            flash(f"Error en la consulta: {str(e)}", 'danger')
        return redirect(url_for('main.index'))
    return render_template('query.html')
