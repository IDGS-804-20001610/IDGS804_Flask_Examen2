from flask import Blueprint, render_template, redirect, url_for, request, flash
from project.models import Alumnos

from project.forms import AlumnosForm

from project import db 

students = Blueprint('students', __name__, url_prefix='/students')

@students.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = AlumnosForm(request.form)
    if request.method == 'POST':
        alu = Alumnos(nombre = create_form.nombre.data,
                      apaterno = create_form.apaterno.data,
                      amaterno = create_form.amaterno.data,
                      email = create_form.email.data,
                      carrera = create_form.carrera.data)
        db.session.add(alu)
        db.session.commit()
        return redirect(url_for('students.read'))
    return render_template('create_alumnos.html', form = create_form)

@students.route('/read', methods = ['GET', 'POST'])
def read():
    read_form = AlumnosForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template('read_alumnos.html', form = read_form, alumnos = alumnos)

@students.route('/update', methods = ['GET', 'POST'])
def update():
    update_form = AlumnosForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        alu = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        update_form.id.data = request.args.get('id')
        update_form.nombre.data = alu.nombre
        update_form.apaterno.data = alu.apaterno
        update_form.amaterno.data = alu.amaterno
        update_form.email.data = alu.email
        update_form.carrera.data = alu.carrera

    if request.method == 'POST':
        id = update_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = update_form.nombre.data
        alum.apaterno = update_form.apaterno.data
        alum.amaterno = update_form.amaterno.data
        alum.email = update_form.email.data
        alum.carrera = update_form.carrera.data

        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('students.read'))
    
    return render_template('update_alumnos.html', form = update_form)

@students.route('/delete', methods = ['GET', 'POST'])
def delete():
    delete_form = AlumnosForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        alu = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        delete_form.id.data = request.args.get('id')
        delete_form.nombre.data = alu.nombre
        delete_form.apaterno.data = alu.apaterno
        delete_form.amaterno.data = alu.amaterno
        delete_form.email.data = alu.email
        delete_form.carrera.data = alu.carrera

    if request.method == 'POST':
        id = delete_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = delete_form.nombre.data
        alum.apaterno = delete_form.apaterno.data
        alum.amaterno = delete_form.amaterno.data
        alum.email = delete_form.email.data
        alum.carrera = delete_form.carrera.data

        db.session.delete(alum)
        db.session.commit()
        
        return redirect(url_for('students.read'))

    return render_template('delete_alumnos.html', form = delete_form)