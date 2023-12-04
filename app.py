from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_cors import cross_origin
import json
import database.DB as DB


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/remontadas")
def remontadas():
    return render_template('remontadas.html')

@app.route("/arbitros")
def arbitros():
    return render_template('arbitros.html')

@app.route("/versus", methods=('POST', 'GET'))
def versus():
    tabla=False
    error=False
    equipos = DB.equipos()
    if(request.method=='POST'):
        equipo1 = request.form.get('equipo1')
        equipo2 = request.form.get('equipo2')
        goles = DB.versusGoles(equipo1,equipo2)
        fouls = DB.versusFouls(equipo1,equipo2)
        if goles:
            tabla=True
        else:
            error = True
        return render_template('versus.html',equipos=equipos,goles=goles,fouls=fouls,tabla=tabla,error=error)
    else:
        return render_template('versus.html',equipos=equipos,tabla=tabla,error=error)



@app.route("/remontadores")
@cross_origin(origin="localhost", supports_credentials=True)
def remontadores():
    data = {}
    for dato in DB.remontadores():
        data[dato[0]]=dato[1]
    return jsonify(data)

@app.route("/remontados")
@cross_origin(origin="localhost", supports_credentials=True)
def remontados():
    data = {}
    for dato in DB.remontados():
        data[dato[0]]=dato[1]
    return jsonify(data)

@app.route("/amarillas")
@cross_origin(origin="localhost", supports_credentials=True)
def amarillas():
    data = {}
    for dato in DB.amarillas():
        data[dato[0]]=int(dato[1])
    return jsonify(data)

@app.route("/rojas")
@cross_origin(origin="localhost", supports_credentials=True)
def rojas():
    data = {}
    for dato in DB.rojas():
        data[dato[0]]=int(dato[1])
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)