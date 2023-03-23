from flask import Flask
from flask_wtf.csrf import CSRFProtect

from .models import db
import os

from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/examen2'
    csrf = CSRFProtect()
    
    csrf.init_app(app)
    db.init_app(app)
    '''@app.before_first_request
    def create_all():
        db.create_all()
'''
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .students.rouetes import students as students_blueprint
    app.register_blueprint(students_blueprint)

    from .teachers.routes import teachers as teachers_blueprint
    app.register_blueprint(teachers_blueprint)

    return app