from wtforms import Form, StringField, IntegerField, EmailField, validators

class AlumnosForm(Form):
    id = IntegerField('ID', [validators.number_range(min = 1, max = 20, message = 'id NO válido')])
    nombre = StringField('NOMBRE(S)', [validators.DataRequired(message = 'Nombre NO váido')])
    apaterno = StringField('APELLIDO PATERNO', [validators.DataRequired(message = 'Apellido NO váido')])
    amaterno = StringField('APELLIDO MATERNO', [validators.DataRequired(message = 'Apellido NO váido')])
    email = EmailField('CORREO', [validators.DataRequired(message =  'Correo NO válido'), validators.Email(message = 'Ingresa un correo válido')])
    carrera = StringField('CARRERA', [validators.DataRequired(message = 'Carrera NO váido')])

class MaestrosForm(Form):
    id = IntegerField('ID', [validators.number_range(min = 1, max = 20, message = 'id NO válido')])
    nombre = StringField('NOMBRE(S)', [validators.DataRequired(message = 'Nombre NO váido')])
    apaterno = StringField('APELLIDO PATERNO', [validators.DataRequired(message = 'Apellido NO váido')])
    amaterno = StringField('APELLIDO MATERNO', [validators.DataRequired(message = 'Apellido NO váido')])
    email = EmailField('CORREO', [validators.DataRequired(message =  'Correo NO válido'), validators.Email(message = 'Ingresa un correo válido')])
    telefono = StringField('NÚMERO TELEFÓNICO', [validators.DataRequired(message = 'Número Telefónico NO váido'), validators.number_range(min = 10, max = 10)])