from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import Maestros

from .forms import MaestrosForm

from . import db 
from .db import get_connection

from .procedures import get_teachers

teachers = Blueprint('teachers', __name__, url_prefix='/teachers')

@teachers.route('/create', methods=['GET', 'POST'])
def create_maestros():
    create_form = MaestrosForm(request.form)

    if (request.method == 'POST'):
        name = create_form.nombre.data
        apa = create_form.apaterno.data
        ama = create_form.amaterno.data
        ema = create_form.email.data
        tel = create_form.telefono.data

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL create_maestro(%s, %s, %s, %s, %s)', 
                       (name, apa, ama, ema, tel))
        connection.commit()
        connection.close()
        return redirect(url_for('teachers.read_maestros'))

    return render_template('create_maestros.html', form = create_form)

@teachers.route('/read', methods = ['GET', 'POST'])
def read_maestros():
    read_form = MaestrosForm(request.form)

    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('CALL get_maestros()')
        teachers = cursor.fetchall()
    return render_template('read_maestros.html', teachers = teachers, form = read_form)

@teachers.route('/update', methods = ['GET', 'POST'])
def update_maestros():
    update_form = MaestrosForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        print(id)
        teach = db.session.query(Maestros).filter(Maestros.id == id).first()
        update_form.id.data = request.args.get('id')
        
        update_form.nombre.data = teach.nombre
        update_form.apaterno.data = teach.apaterno
        update_form.amaterno.data = teach.amaterno
        update_form.email.data = teach.email
        update_form.telefono.data = teach.telefono

    if (request.method == 'POST'):
        id = update_form.id.data
        name = update_form.nombre.data
        apa = update_form.apaterno.data
        ama = update_form.amaterno.data
        ema = update_form.email.data
        tel = update_form.telefono.data
        
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL update_maestro(%s, %s, %s, %s, %s, %s)', 
                       (id, name, apa, ama, ema, tel))
        connection.commit()
        connection.close()
        return redirect(url_for('teachers.read_maestros'))

    return render_template('update_maestros.html', form = update_form)

@teachers.route('/delete', methods = ['GET', 'POST'])
def delete_maestros():
    delete_form = MaestrosForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        print(id)
        teach = db.session.query(Maestros).filter(Maestros.id == id).first()
        delete_form.id.data = request.args.get('id')
        
        delete_form.nombre.data = teach.nombre
        delete_form.apaterno.data = teach.apaterno
        delete_form.amaterno.data = teach.amaterno
        delete_form.email.data = teach.email
        delete_form.telefono.data = teach.telefono

    if (request.method == 'POST'):
        id = delete_form.id.data
        
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL delete_maestro(%s)', 
                       (id))
        connection.commit()
        connection.close()
        return redirect(url_for('teachers.read_maestros'))
    return render_template('delete_maestros.html', form = delete_form)