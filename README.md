# IV- Bot de telegram para consultar los resultados de las sesiones de moto GP

## Proyecto a realizar

[![Build Status](https://travis-ci.org/Miguelmoral/IV.svg?branch=master)](https://travis-ci.org/Miguelmoral/IV)

Se va a llevar a cabo la realización de un bot de Telegram para ver información sobre los grandes premios de Moto GP pudiendo hacer consultas de posición de los pilotos o tiempos de estos en distintos grandes premios que se hayan corrido. Para ello se hará uso del web scraping sacando de está forma los datos que nos sean útiles. La web que he elegido para coger la información es esta en concreto ya que el formato no varia, tan solo cambia para los grandes premios que se han corrido en 2016 pero ese problema se puede solucionar de forma facil ya que todos los grandes premios de 2016 tienen el mismo formato entre ellos.

## Servicios que se van a utilizar:
- Herramienta aún por determinar para escrapear los datos de la web de donde se quiere extraer la información.
- Phyton para desarrollar el bot.
- Servidor de base de datos.
- Despliege en la nube.
- Monitorización.

## Como usar:

Para ejecutar el bot introduciremos `python bot.py` , una vez que el bot se está ejecutando podremos introducir los siguientes comandos:

- `/carreras`  #Devolverá una lista con las carreras disponibles y su correspondiente código que nos servirá para el comando /resultados
- `/resultados AÑO COD_CARRERA SESION` #Con este comando el bot nos mostrará los resultados en el año y carrera seleccionados, opcionalmente se podrá pasar el argumento sesión(Q1,Q2), en caso de dejar el espacio en blando por defecto mostrará los resultados de la sesión carrera.



