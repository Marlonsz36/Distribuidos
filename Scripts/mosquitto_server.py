#!/usr/bin/env python 1
# -*- coding: utf-8 -*-
#@author Marlon Segarra, Cesar Navas
#Proyecto de Redes de sensores
#Paralelo # 1
#Grupo #6
#Término 2019 1S
import paho.mqtt.client as mqtt
import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
#import reconocer
cnt=0



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Conectado - Codigo de resultado: " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("id_huella")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    #lista = msg.topic.split("/")
    print(str(msg.payload))
    # Abrir conexión con bases de datos
    try:
   	 db = MySQLdb.connect("127.0.0.1", "marlon", "xxxxxx", "prueba_huella")
    except:
    	print("No se pudo conectar con la base de datos")
    	print("Cerrando...")
    	sys.exit()
    # Preparando cursor
    cursor = db.cursor()
    sql = """UPDATE `prueba_huella`.`asistencia` SET atento=2 WHERE HuellaID=3"""
    #inputData = str(msg.payload)[2:3]
    try:
    	# Ejecutar un comando SQL
    	#print("entro")
    	cursor.execute(sql)
    	#print("ejecuto")
    	db.commit()
    	db.close()
    	print("Guardando en base de datos...OK")
    except:
        db.rollback()
        print("Guardando en base de datos...Falló")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("192.168.2.210", 1883)
except:
    print("No se pudo conectar con el MQTT Broker...")
    print("Cerrando...")
    sys.exit()

client.username_pw_set("marlon", "xxxxxxxx")

try:
    client.loop_forever()
except KeyboardInterrupt:  # precionar Crtl + C para salir
    print("Cerrando...")
    db.close()
