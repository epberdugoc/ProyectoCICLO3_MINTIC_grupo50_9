from flask_wtf import FlaskForm
#from flask_wtf.recaptcha import validators

from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired



class Empleados( FlaskForm ):
    cedula=IntegerField('cedula', validators=[DataRequired("No dejar vacio")])
    nombres=StringField('nombres', validators=[DataRequired("No dejar vacio")])
    apellidos=StringField('apellidos', validators=[DataRequired("No dejar vacio")])
    fechaingreso=StringField('fechaingreso', validators=[DataRequired("No dejar vacio")])
    tipocontrato=StringField('tipocontrato', validators=[DataRequired("No dejar vacio")])
    terminocontrato=StringField('terminocontrato', validators=[DataRequired("No dejar vacio")])
    cargo=StringField('cargo', validators=[DataRequired("No dejar vacio")])
    dependencia=StringField('dependencia', validators=[DataRequired("No dejar vacio")])
    salario=IntegerField('salario', validators=[DataRequired("No dejar vacio")])
    enviar=SubmitField('Agregar Empleado')
    consultar=SubmitField('consultar empleado')
    editar=SubmitField('editar empleado')
    eliminar=SubmitField('eliminar empleado')
    
    