---
layout: index
---

## Práctica 0

### 1-Creación de una llave ssh y añadir esta a github:
Creación de claves ssh:

`ssh-keygen -t rsa -C "miguelmoralllamas@correo.ugr.es"`

Vemos la clave que hemos generado para poder introducirla en nuestro github:

`cat /home/miguel/.ssh/id_rsa.pub`

Una vez sabemos la clave que hemos generado tan solo nos quedará introducirla en github mediante su interfaz gráfica de una forma sencilla.

###  2- Creación de un repositorio personal para la asignatura y fork del repositorio de la asignatura.

Estás dos operaciones se llevarán a cabo desde la interfaz gráfica de github.

### 3- Creación de una nueva rama hito0 en nuestro repositorio personal que nos servirá para alojar la práctica0

Para crear esta nueva rama tan solo tendremos que crearla haciendo click en la opción branch que nos aparecerá en nuestro repositorio personal en la interfaz de github.

### 4- Asignación de nombre y correo para commits

Para que aparezca esta información cuando realicemos un commit ejecutaremos los siguientes comandos :

`git config --global user.name "Miguelmoral"`

`git config --global user.email "miguelmoralllamas@correo.ugr.es"`

### 5- Creación del milestone práctica0 y sus correspondientes issues

La interfaz de github nos permite crear y manejar milestones e issues de una manera sencilla, tan solo tendremos que crear un nuevo milestone llamado práctica 0 y una vez que pinchemos sobre este milestone nos dará la opción de crear distintos issues para alcanzar el milestone. Conforme vallamos completando y eliminando los issues que realicemos se nos mostrará el porcentaje de issues que nos queda para completar el milestone.

### 6- Creación de los archivos README, LICENSE y gitignore

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






