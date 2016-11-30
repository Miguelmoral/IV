---
layout: index
---

## Práctica 0

## 1-Creación de una llave ssh y añadir esta a github:
Creación de claves ssh:

`ssh-keygen -t rsa -C "miguelmoralllamas@correo.ugr.es"`

Vemos la clave que hemos generado para poder introducirla en nuestro github:

`cat /home/miguel/.ssh/id_rsa.pub`

Una vez sabemos la clave que hemos generado tan solo nos quedará introducirla en github mediante su interfaz gráfica de una forma sencilla.

##  2- Creación de un repositorio personal para la asignatura y fork del repositorio de la asignatura.

Estás dos operaciones se llevarán a cabo desde la interfaz gráfica de github.

## 3- Creación de una nueva rama hito0 en nuestro repositorio personal que nos servirá para alojar la práctica0

Para crear esta nueva rama tan solo tendremos que crearla haciendo click en la opción branch que nos aparecerá en nuestro repositorio personal en la interfaz de github.

## 4- Asignación de nombre y correo para commits

Para que aparezca esta información cuando realicemos un commit ejecutaremos los siguientes comandos :

`git config --global user.name "Miguelmoral"`

`git config --global user.email "miguelmoralllamas@correo.ugr.es"`

## 5- Creación del milestone práctica0 y sus correspondientes issues

La interfaz de github nos permite crear y manejar milestones e issues de una manera sencilla, tan solo tendremos que crear un nuevo milestone llamado práctica 0 y una vez que pinchemos sobre este milestone nos dará la opción de crear distintos issues para alcanzar el milestone. Conforme vallamos completando y eliminando los issues que realicemos se nos mostrará el porcentaje de issues que nos queda para completar el milestone.

## 6- Creación de los archivos README, LICENSE y gitignore

Una vez creemos estos archivos en local los subiremos mediante git con los siguientes comandos:


`git add .`


` git commit -m "Incorporación de archivos README, LICENSE y gitignore" `


`git push origin hito0`


## Primer hito: Estructuración del proyecto

### Prerrequisitos
- [x]Tener aprobado el hito 0 de proyecto.
- [x]Haber alcanzado el 80% de los objetivos del tema introductorio.
- [x]Haber realizado los ejercicios propuestos.


### Explicación del proyecto a realizar:

Se va a llevar a cabo la realización de un bot de Telegram para ver información sobre los grandes premios de Moto GP pudiendo hacer consultas de posición de los pilotos o tiempos de estos en distintos grandes premios que se hayan corrido. Para ello se hará uso del web scraping sacando de está forma los datos que nos sean útiles. La web que he elegido para coger la información es [esta](http://www.motogp.com/es/ajax/results/parse/2014/ARA/MotoGP/Q2) en concreto ya que el formato no varia, tan solo cambia para los grandes premios que se han corrido en 2016 pero ese problema se puede solucionar de forma facil ya que todos los grandes premios de 2016 tienen el mismo formato entre ellos.

### Servicios:

- Herramienta aún por determinar para escrapear los datos de la web de donde se quiere extraer la información.
- Phyton para desarrollar el bot.
- Servidor de base de datos.
- Despliege en la nube.
- Monitorización.

## Segundo hito:

### Descripción del proyecto:

El proyecto sobre el que se van a realizar lso tests de integración continua es un bot de telegram al cuál le podremos consultar los resultados de distintas sesiones y este bot nos responderá con esta información.

### Prerrequisitos:

Haber alcanzado el 80% de los objetivos del tema introductorio tras haber realizado los ejercicios propuestos [ejercicios](https://github.com/Miguelmoral/IVejercicios/blob/master/tema2.md).

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

En primer lugar tedremos que hacer un documento Dockerfile como este en nuestro repositorio de github:

```
FROM ubuntu:14.04
MAINTAINER Miguel Moral Llamas <miguelmoralllamas@correo.ugr.es>
ARG TOKENMOTOGP
ARG DATABASE_URL

ENV TOKENMOTOGP=$TOKENMOTOGP
ENV DATABASE_URL=$DATABASE_URL

#instalamos git
RUN apt-get -y update
RUN apt-get install -y git

#Clonamos repositorio
RUN sudo git clone https://github.com/Miguelmoral/IV

#Instalamos herramientas
RUN sudo apt-get -y update
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip



RUN cd IV/ && make install
```

A continuación tendremos que registrarnos en docker hub si no tenemos cuenta y enlazarla con nuestro github.

Tendremos que hacer click en create automated build y automáticamente cogerá nuestro archivo dockerfile. Si todo ha salido correctamente nos mostrará lo siguiente en la web de docker hub:

![docker](http://i67.tinypic.com/33zd6s7.png)

En este momento podremos ejecutar la imagen con los siguientes comandos `sudo docker pull miguemoral/iv` y `sudo docker run -e "TOKENMOTOGP=270820377:AAE8J3ISnM9LQUOl2dViqTHpRe_4w75LDW0" -e "DATABASE_URL=postgres://duhfjfoqfomzvy:WSWZd5PeQ8wGCkIyYF-rwlFiEn@ec2-23-23-76-90.compute-1.amazonaws.com:5432/de7bsh4d838oe1" -i -t miguelmoral/iv /bin/bash`

Una ven dentro de la máquina tendremos que dirigirnos al directorio IV y ejecutar `make ejecutar`

Enlace a dockers [![Docker](https://camo.githubusercontent.com/8a4737bc02fcfeb36a2d7cfb9d3e886e9baf37ad/687474703a2f2f693632382e70686f746f6275636b65742e636f6d2f616c62756d732f7575362f726f6d696c67696c646f2f646f636b657269636f6e5f7a7073776a3369667772772e706e67)](https://hub.docker.com/r/miguelmoral/iv/)





