# IV- Bot de telegram para consultar los resultados de las sesiones de moto GP

## Proyecto a realizar

[![Build Status](https://travis-ci.org/Miguelmoral/IV.svg?branch=master)](https://travis-ci.org/Miguelmoral/IV)
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://lit-spire-74429.herokuapp.com/) 
[![Docker](https://camo.githubusercontent.com/8a4737bc02fcfeb36a2d7cfb9d3e886e9baf37ad/687474703a2f2f693632382e70686f746f6275636b65742e636f6d2f616c62756d732f7575362f726f6d696c67696c646f2f646f636b657269636f6e5f7a7073776a3369667772772e706e67)](https://hub.docker.com/r/miguelmoral/iv/)

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

### Despliegue en un pass:

Para el despliegue me he decidido por utilizar Heroku para desplegar mi aplicación. Una vez nos registremos en la web Heroku tendremos que crear un nuevo proyecto y una base de datos asociada a este, para ello ejecutaremos los siguientes comandos, para la creación de la aplicación `heroku create` y para la creación de la base de datos `heroku addons:create heroku-postgresql:hobby-basic` . Podremos ver en la web de Heroku que tanto la aplicación como la base de datos están correctamente creadas. El siguiente paso será enlazar nuestra cuenta de github con Heroku. Para ello tan solo tendremos que acceder a account settings y activarlo

![heroku-github](http://i64.tinypic.com/13z4rnp.png)

Una vez hecho tendremos que seleccionar el repositorio de GitHub que queremos enlazar con Heroku para que nuestra app se suba de forma correcta.
Podremos gestionar la base de datos que hemos creado en Heroku desde la terminal de nuestro PC, para ello necesitaremos acceder a las credenciales de nuestra base de datos, en la sección databases podremos acceder a la información de todas las bases de datos que tengamos creadas (En caso de estar trabajando con una cuenta gratuita sin introducir tarjeta de crédito el número máximo tanto de aplicaciones como de bases de datos será 4). Esta es toda la información que nos aporta Heroku sobre las bases de datos, para conectarnos a ella tendriamos que introducir un comando especificado en las credenciales (en la captura no se muestran las credenciales por motivos de seguridad)

![imagendb](http://i68.tinypic.com/dm8uoh.png)

En este momento tenemos nuestra aplicación de github enlazada con Heroku tan solo nos quedaría crear un archivo Procfile para la ejecución en Heroku en nuestro repositorio con el siguiente contenido:

```
worker: python bot_motoGP/bot.py

```
Además tendremos que declarar tanto en Heroku como en TravisCI las variables de entorno con el Token del bot de Telegram como el de la DATABASE_URL para poder acceder a la DB creada en Heroku que está enlazada con el proyecto de Heroku.

El último paso será configurar en Heroku que se realice el deploy tan solo cuando se pasen correctamente los test unitarios para ello nos tendremos que dirigir a la sección deploy de nuestra aplicación, una vez que la tenemos configurada correctamente debería tener un aspecto similar a este:

![finalapp](http://i67.tinypic.com/x4kisy.png)

Una vez que se evaluen los test unitarios de nuestra aplicación en TravisCI en mi caso veremos como nuestra aplicación se despliega en Heroku:

![deployapp](http://i64.tinypic.com/2wcfwxt.png)

En este momento nuesto bot esta desplegado y es totalmente funcional. Podemos ver los logs introduciendo en la carpeta donde se encuentre nuestro bot el comando`heroku logs --tail` y podemos ver como ejecuta los comandos que queramos sin nigún problema además de estar funcionando el bot.

![logs](http://i67.tinypic.com/fbjau1.png)

Podremos ver que el bot funcina perfectamente hablándole (alias del bot @Prueba567_bot)

### Entorno de pruebas:

Para descargar el contenedor de docker tendremos que ejecutar:
- `sudo docker pull miguemoral/iv`
- `sudo docker run -e "TOKENMOTOGP=INTRODUCIR_TOKEN_DEL_BOT" -e "DATABASE_URL=INTRODUCIR_URL_DE_LA_BD" -i -t miguelmoral/iv /bin/bash`

Una vez estemos dentro:
- `cd IV`
- `make ejecutar`







