# -*- coding: utf-8 -*-
import types
import requests


def comprobacion_errores(anio, pais):
    if not anio.isnumeric():
        return "La fecha introducida ha de ser un numero"
    elif anio > "2016":
        return "Fecha incorrecta, tiene que introducir un año menor que 2016"
    elif anio < "2002":
        return "Fecha incorrecta, tiene que introducir un año mayor que 2002"
    elif pais.isnumeric():
        bot.send_message(cid, "La carrera introducida ha de ser un código de 3 letras. Vease comando /carreras")
    else:
        return True


def get_url(anio,pais,sesion):
    cadenaurl = "http://www.motogp.com/es/ajax/results/parse/" + str(anio) + "/" + str(pais) +"/MotoGP/" + str(sesion)
    url = cadenaurl
    # Realizamos la petición a la web
    req = requests.get(url)
    return req
