# -*- coding: utf-8 -*-
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import os
import sqlite3
import modules
from bs4 import BeautifulSoup
import requests
import types
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])



bot = telebot.TeleBot(os.environ["TOKENMOTOGP"]) # Creamos el objeto de nuestro bot.

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	bot.send_message(cid, "Introduzca uno de los comandos aquí especificados\nListado de comandos: \n-/carreras -> Devolverá una lista con todas las posibles carreras sobre las que hacer una consulta con el correspondiente código el cuál tendremos que utilizar para realizar la consulta\n- /resultados año codigo_carrera sesion -> Con este comando podremos consultar los resultados de una determinada carrera introduciendo los parámetros año (ej: 2015) coódigo de la carrera (ej: ARA) sesión (Este parámetro es opcional si se deja en blanco mostrá los resultados de la carrera ej:Q2)\nUn ejemplo de uso para el comando /resultados seria:\n/resultados 2015 ARA Q2 -> Este comando nos devolverá los resultados del gran premio de aragón de 2015 en la sesión Q2")


@bot.message_handler(commands=['carreras'])
def command_carreras(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    cadena = "Posibles carreras para seleccionar:" + "\n"

    try:
        # con_bd = psycopg2.connect(database='d8jve0c750bc8r',user='hhggnmpsqdfffc',password='1L0f3Z5j4niLnOrtNo-qKnbjig',host='ec2-50-17-220-39.compute-1.amazonaws.com')
        #con_bd = psycopg2.connect(database='motogpbot',user='miguel',password='miguel',host='localhost')
        con_bd = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        cur = con_bd.cursor()
    	cur.execute("SELECT * FROM datos")
        rows = cur.fetchall()
        for row in rows:
            cadena += row[0] + row[1] + "\n"
    	cur.close()
    	con_bd.close()
    except:
        cadena = "No se puede conectar a la bd"


    bot.send_message(cid,cadena)


@bot.message_handler(commands=['fecha'])
def command_fecha(m):
    cid = m.chat.id
    x = datetime.datetime.now()
    switcher = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
    mes = switcher[x.month]
    fecha = "Estamos a %s de %s" % (x.day, mes)
    bot.send_message(cid, fecha)

@bot.message_handler(commands=['resultados'])
def command_resultados(m):
    cid = m.chat.id
    anio = m.text[12:16] # Definimos el tamaño que va a tener anio y le asignamos el valor que le pasamos por parámetros
    pais = m.text[17:20]
    sesion = m.text[21:]
    cadena = " "
    contador = 1

    #-------------------------------------------------Comprobación de errores--------------------------------#
    resmen= modules.comprobacion_errores(anio,pais)
    if type(resmen) != types.BooleanType:
        bot.send_message(cid, resmen)
    else:
        req = modules.get_url(anio,pais,sesion)
        statusCode = req.status_code
        htmlText = req.text

        if statusCode == 200:

            try:
                # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
                html = BeautifulSoup(req.text, "html.parser")


                # Para eliminar el primer enlace ya que no nos interesa que se muestre
                final_link = html.p.a
                final_link.decompose()
            except:
                bot.send_message(cid, "Error formato incorrecto. El formato correcto es:" + "\n" + "/resultados yyyy GP Sesión")
            # Buscamos todos los enlaces
            links = html.find_all('a')

            for link in links:
                if contador<13:
                    names = link.contents[0]
                    cadena += "-Posición " + str(contador) + ": " + names.encode('utf8') + "\n"
                    contador = contador + 1

            bot.send_message(cid, cadena)


        else:
            print "Status Code %d" %statusCode

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
