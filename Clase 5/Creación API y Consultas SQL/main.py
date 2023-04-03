from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
import cx_Oracle
import sql

username = 'ldecast'
password = 'ldecast'
dsn = '35.226.27.222/ORCL18'
port = 1521
encoding = 'UTF-8'

app=Flask(__name__)
CORS(app)
api=Api(app)

@app.route("/",methods=['GET'])
def inicio():
    return jsonify({'Respuesta':'Conexion Establecida'})

@app.route("/getPersona",methods=['GET'])
def getPersona():
    try:
        connection = cx_Oracle.connect(
            username,
            password,
            dsn,
            encoding=encoding)
        
        
        json=[]
        c=connection.cursor()
        c.execute(sql.selectPersona)
        for row in c:
            json.append({"ID Persona":str(row[0]),"Nombre":str(row[1]),"Apellido":str(row[2]),"Direccion":str(row[3])})
        
        return jsonify(json)
    except cx_Oracle.Error as error:
        print("error")
        return jsonify({'Response':'Error'})
    finally:
        if connection:
            connection.close()

@app.route("/consulta1",methods=['GET'])
def consulta1():
    try:
        connection = cx_Oracle.connect(
            username,
            password,
            dsn,
            encoding=encoding)
        
        
        json=[]
        c=connection.cursor()
        c.execute(sql.consulta1)
        for row in c:
            json.append({"Nombre":str(row[0]),"Direccion":str(row[1]),"Cantidad":str(row[2])})
        
        return jsonify(json)
    except cx_Oracle.Error as error:
        print("error")
        return jsonify({'Response':'Error'})
    finally:
        if connection:
            connection.close()

@app.route("/consulta2",methods=['GET'])
def consulta2():
    try:
        connection = cx_Oracle.connect(
            username,
            password,
            dsn,
            encoding=encoding)
        
        
        json=[]
        c=connection.cursor()
        c.execute("select * from hospital where id_hospital=6")
        for row in c:
            json.append({"ID Hospital":str(row[0]),"Nombre":str(row[1]),"Direccion":str(row[2])})
        
        return jsonify(json)
    except cx_Oracle.Error as error:
        print("error")
        return jsonify({'Response':'Error'})
    finally:
        if connection:
            connection.close()

if __name__=='__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')