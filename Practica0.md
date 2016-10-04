### Práctica 0
## 1-Creación de una llave ssh y añadir esta a github:
Creación de claves ssh:
```
ssh-keygen -t rsa -C "miguelmoralllamas@correo.ugr.es"
```
Vemos la clave que hemos generado para poder introducirla en nuestro github:
```
cat /home/miguel/.ssh/id_rsa.pub
```
Una vez sabemos la clave que hemos generado tan solo nos quedará introducirla en github mediante su interfaz gráfica de una forma sencilla.
##  2- Creación de un repositorio personal para la asignatura y fork del repositorio de la asignatura.
Estás dos operaciones se llevarán a cabo desde la interfaz gráfica de github.
## 3- Creación de una nueva rama hito0 en nuestro repositorio personal que nos servirá para alojar la práctica0
Para crear esta nueva rama tan solo tendremos que crearla haciendo click en la opción branch que nos aparecerá en nuestro repositorio personal en la interfaz de github.
## 4- Asignación de nombre y correo para commits
Para que aparezca esta información cuando realicemos un commit ejecutaremos los siguientes comandos :
```
git config --global user.name "Miguelmoral"

```
```
git config --global user.email "miguelmoralllamas@correo.ugr.es"

```

## 5- Creación del milestone práctica0 y sus correspondientes issues
La interfaz de github nos permite crear y manejar milestones e issues de una manera sencilla, tan solo tendremos que crear un nuevo milestone llamado práctica 0 y una vez que pinchemos sobre este milestone nos dará la opción de crear distintos issues para alcanzar el milestone. Conforme vallamos completando y eliminando los issues que realicemos se nos mostrará el porcentaje de issues que nos queda para completar el milestone.
## 6- Creación de los archivos README, LICENSE y gitignore
Una vez creemos estos archivos en local los subiremos mediante git con los siguientes comandos:
```
git add .

```
```
git commit -m "Incorporación de archivos README, LICENSE y gitignore"

```
```
git push origin hito0

```




