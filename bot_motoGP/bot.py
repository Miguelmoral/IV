# -*- coding: utf-8 -*-
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import os
import sqlite3


bot = telebot.TeleBot(os.environ["TOKENMOTOGP"]) # Creamos el objeto de nuestro bot.

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start

@bot.message_handler(commands=['carreras'])
def command_carreras(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    cadena = "Posibles carreras para seleccionar:" + "\n"

    con_bd = sqlite3.connect('gp.db')
    cursor_gp = con_bd.cursor()
    cursor_gp.execute("SELECT * FROM CARRERAS")
    for registro in cursor_gp:
        cadena += str(registro) + "\n"
    bot.send_message(cid,cadena)
    cursor_gp.close()
    con_bd.close()

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
    if not anio.isnumeric():
        bot.send_message(cid, "La fecha introducida ha de ser un numero")
    elif anio > "2016":
        bot.send_message(cid, "Fecha incorrecta, tiene que introducir un año menor que 2016")
    elif anio < "2002":
        bot.send_message(cid, "Fecha incorrecta, tiene que introducir un año mayor que 2002")
    elif pais.isnumeric():
        bot.send_message(cid, "La carrera introducida ha de ser un código de 3 letras. Vease comando /carreras")
    else:

        from bs4 import BeautifulSoup
        import requests

        cadenaurl = "http://www.motogp.com/es/ajax/results/parse/" + str(anio) + "/" + str(pais) +"/MotoGP/" + str(sesion)

        url = cadenaurl
        # Realizamos la petición a la web
        req = requests.get(url)

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
