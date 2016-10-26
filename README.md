# IV- Bot de telegram para consultar los resultados de las sesiones de moto GP

## Proyecto a realizar

[![Build Status](https://travis-ci.org/Miguelmoral/IV.svg?branch=master)](https://travis-ci.org/Miguelmoral/IV)

Se va a llevar a cabo la realización de un bot de Telegram para ver información sobre los grandes premios de Moto GP pudiendo hacer consultas de posición de los pilotos o tiempos de estos en distintos grandes premios que se hayan corrido. Para ello se hará uso del web scraping sacando de está forma los datos que nos sean útiles. La web que he elegido para coger la información es esta en concreto ya que el formato no varia, tan solo cambia para los grandes premios que se han corrido en 2016 pero ese problema se puede solucionar de forma facil ya que todos los grandes premios de 2016 tienen el mismo formato entre ellos.

## Servicios que se van a utilizar:
- Herramienta beautifulsoup para escrapear los datos de la web de donde se quiere extraer la información.
- Phyton para desarrollar el bot.
- Servidor de base de datos sqlite.
- Despliege en la nube.
- Monitorización.

### Descripción del proyecto:

El proyecto sobre el que se van a realizar lso tests de integración continua es un bot de telegram al cuál le podremos consultar los resultados de distintas sesiones y este bot nos responderá con esta información.


### Integración continua:

En esta práctica he utilizado travis CI para realizar los test de integración continua, para que travis analice nuestro repositorio tendremos que incluir un fichero .travis.yml cuyo contenido ha de ser parecido al siguiente:

```
language: python
python:
  - "2.7"

# command to install dependencies
install: make install

# command to run tests
script: make test

```

Para que nos funcione tendremos que hacer un Makefile de este estilo:

```

install:
	pip install -r requirements.txt

test:
	cd bot_motoGP && python tests.py

ejecutar:
	cd bot_MotoGP && python bot.py

```

Como la aplicación utiliza un token el cuál no está incluido en el código por motivos de privacidad, tendremos que crearnos en Travis una variable de entorno con dicho token para que pueda ejecutar nuestra aplicación. Esta opción de añadir una variable de entorno la encontraremos en el apartado settings del repositorio que deseemos dentro de la web de Travis.

Una vez subamos nuestro proyecto a github y habilitemos en travis ese repositorio empezará a ejecutar los test mostrándonos la siguiente imagen, en la cuál podemos ver que se han ejecutado 3 test de forma exitosa:

![imagenTravis](http://i64.tinypic.com/262r6mv.png)

Si todo está correcto y se pasa el test travis nos mostrará lo siguiente 

[![Build Status](https://travis-ci.org/Miguelmoral/IV.svg?branch=master)](https://travis-ci.org/Miguelmoral/IV)



## Como usar:

Para ejecutar el bot introduciremos `python bot.py` , una vez que el bot se está ejecutando podremos introducir los siguientes comandos:

- `/carreras`  #Devolverá una lista con las carreras disponibles y su correspondiente código que nos servirá para el comando /resultados
- `/resultados AÑO COD_CARRERA SESION` #Con este comando el bot nos mostrará los resultados en el año y carrera seleccionados, opcionalmente se podrá pasar el argumento sesión(Q1,Q2), en caso de dejar el espacio en blando por defecto mostrará los resultados de la sesión carrera.



