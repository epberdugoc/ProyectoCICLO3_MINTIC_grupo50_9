from flask import Flask
from flask import render_template as render
from flask import request
from db import sql_connection
from forms import Empleados
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom( 24 )


 
@app.route('/', methods=["GET"])
def inicio():
    return render("inicio.html")

@app.route("/registro",  methods=["GET", "POST"])
def registrarse():
    return "pagina de registro"

@app.route("/ingreso", methods=["GET", "POST"])
def ingresar():
    if request.method=="GET":
        return render("ingreso.html")
    else:
        return render("dashboard.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return "pagina de dashboard"

@app.route("/buscar", methods=["GET", "POST"]) 
def buscar():
    if request.method=="GET":
        form=Empleados()
        return render("buscar.html", form=form)
    
    else:
       form=Empleados()
       ced=request.form['cedula']
       #ced=int(ced)
       #ced=form.cedula.data
       #ced=int(ced)
       con=sql_connection()
       con.row_factory=sqlite3.Row
       cur = con.cursor()
       statemente="SELECT * FROM Empleados WHERE cedula=?"
       cur.execute(statemente,[ced])
       row = cur.fetchone()
       return render('vista_empleado.html', row=row)
       #return render('vista_empleado.html', cur=cur)
       
 

@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method=="GET":
        form=Empleados()
        return render("crear.html", form=form)
       
    else:
        ced=request.form['cedula']
        nom=request.form['nombres']
        ape=request.form['apellidos']
        fing=request.form['fechaingreso']
        tipo=request.form['tipocontrato']
        ter=request.form['terminocontrato']
        car=request.form['cargo']
        depe=request.form['dependencia']
        sal=request.form['salario']
        con=sql_connection()
        cur = con.cursor()
        cur.execute('INSERT INTO Empleados (cedula,nombres,apellidos,fechaingreso,tipocontrato,terminocontrato,cargo,dependencia,salario) VALUES (?,?,?,?,?,?,?,?,?)',(ced, nom, ape, fing, tipo, ter, car, depe, sal))
        con.commit()
        return "Empleado creado"

        
    
    
@app.route("/editar", methods=["GET", "POST"])
def editar():
    if request.method=="GET":
        form=Empleados()
        return render("editar.html", form=form)
       
    else:
        ced=request.form['cedula']
        nom=request.form['nombres']
        ape=request.form['apellidos']
        fing=request.form['fechaingreso']
        tipo=request.form['tipocontrato']
        ter=request.form['terminocontrato']
        car=request.form['cargo']
        depe=request.form['dependencia']
        sal=request.form['salario']
        con=sql_connection()
        cur = con.cursor()
        cur.execute('INSERT INTO Empleados (cedula,nombres,apellidos,fechaingreso,tipocontrato,terminocontrato,cargo,dependencia,salario) VALUES (?,?,?,?,?,?,?,?,?)',(ced, nom, ape, fing, tipo, ter, car, depe, sal))
        con.commit()
        return "Empleado editado"

@app.route("/eliminar", methods=["GET","POST"])
def eliminar():
    if request.method=="GET":
        form=Empleados()
        return render("eliminar.html", form=form)
    else:
        ced=request.form['cedula']
        con=sql_connection()
        cur = con.cursor()
        statemente="DELETE FROM Empleados WHERE cedula=?"
        cur.execute(statemente,[ced])
        con.commit()
        if con.total_changes >0: 
                return "EMPLEADO ELIMINADO"
        else: 
                return "EMPLEADO NO ENCONTRADO"

@app.route("/disponibles", methods=["GET"])
def disponibles():
    con=sql_connection()
    con.row_factory=sqlite3.Row
    cur = con.cursor()
    statemente="SELECT * FROM Empleados"
    cur.execute(statemente)
    row = cur.fetchall()
    return render('disponibles.html', row=row)
       #return render('vista_empleado.html', cur=cur)
       
    #return render("disponibles.html", info_empleado=info_empleado)







if __name__=='__main__':
    app.run(debug=True)

