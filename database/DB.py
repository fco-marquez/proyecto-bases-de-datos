import psycopg2
import psycopg2.extras
import json

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)

def get_conn():
    conn = psycopg2.connect(host="cc3201.dcc.uchile.cl",database ="cc3201",user ="cc3201",password ="eFoot", port ="5513")
    return conn

def remontadores():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["remontadores"])
    remontadores = cursor.fetchall()
    return remontadores

def remontados():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["remontados"])
    remontados = cursor.fetchall()
    return remontados

def amarillas():
     conn = get_conn()
     cursor = conn.cursor()
     cursor.execute(QUERY_DICT["foulsamarillas"])
     amarillas = cursor.fetchall()
     return amarillas

def rojas():
     conn = get_conn()
     cursor = conn.cursor()
     cursor.execute(QUERY_DICT["foulsrojas"])
     rojas = cursor.fetchall()
     return rojas

def versusGoles(equipo1,equipo2):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["versusGoles"],(equipo1,equipo2))
    datos = cursor.fetchone()
    return datos

def versusFouls(equipo1,equipo2):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["versusFouls"],(equipo1,equipo2))
    datos = cursor.fetchone()
    return datos

def equipos():
     conn = get_conn()
     cursor= conn.cursor()
     cursor.execute("SELECT * FROM team ORDER BY name")
     equipos = cursor.fetchall()
     return equipos