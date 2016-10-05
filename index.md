---
layout: index
---

## Ejercicios tema 1

## Ejercicio 1

### Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años.

Para este ejercicio he elegido el servidor de la marca Dell [Dell PowerEdge T430](http://www.dell.com/es/empresas/p/poweredge-t430/pd?oc=pet43002&model_id=poweredge-t430) con un precio sin IVA de  1113 €.

### Amortización a 4 años:
Para la amortización se puede imputar imputar anualmente como gasto deducible en concepto de amortización un máximo del 25%, quedándonos:

- 1113€ * 0,25 = 278,5 € cada año.

### Amortización a 7 años:
En el caso de ser una amortización a 7 años los dos primeros años tendremos un 25% que es el máximo y a partir del tercer año tendremos una amortización del 10%, nos quedaría por tanto:

- Primer y segundo año: 1113€ * 0,25 = 278,5 € cada uno de estos dos años.
- Tercer año: 1113€ * 0,10 = 111,3€
- Cuarto año: 1113€ * 0,10 = 111,3€
- Quinto año: 1113€ * 0,10 = 111,3€
- Sexto año: 1113€ * 0,10 = 111,3€
- Septimo año: 1113€ * 0,10 = 111,3€

## Ejercicio 2

### Usando las tablas de precios de servicios de alojamiento en Internet y de proveedores de servicios en la nube, Comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) en el caso de que la infraestructura comprada se usa sólo el 1% o el 10% del tiempo.

Para este ejercicio se ha utilizado el servidor dedicado de la empresa acens con las siguientes [características](https://panel.acens.net/cart/?_ga=1.116388422.1312366403.1475491454#/dedicados):
- CPU: Intel® Xeon® E3-1230 v5 (4 x 3,4 GHz)
- RAM: 16 GB
- HDD: 2 x 1 TB SATA
- Precio: 99,90 €/mes

Y para el servidos cloud se ha utilizado un servidor de la página 1&1 la cuál nos permite configurar un servidor cloud a nuestra medida con las [características](https://www.1and1.es/servidor-cloud-dinamico#configuracion-del-servidor):
- CPU: 4 vCPU 
- RAM: 16 GB
- HDD: 20 GB SSD (Cabe destacar que no he puesto más capacidad ya que al ser un disco SSD el precio aumentaba demasiado si aumentamos esta memoria)
- Precio: 145,44 €/mes

Vamos a ver los costes durante un año dependiendo de si cada máquina se utiliza un 1% o un 10% del tiempo:
En el caso del servidor dedicado el precio al año va a ser siempre de 99,9*12=1198.8€/año
Vamos a ver ahora el precio del servidor cloud dependiendo del uso que se le de:
- Para un uso del 1%: (145.44*12)*0.01 = 17.45€/año
- Para un uso del 10%: (145.44*12)*0.1 = 174.52€/año
## Ejercicio 3

### Crear un programa simple en cualquier lenguaje interpretado para Linux, empaquetarlo con CDE y probarlo en diferentes distribuciones.

Vamos a instalar CDE con el comando `sudo apt-get instal cde`

Para realizar este ejercicio se va a usar este simple programa:

```
#!/bin/bash

echo "Ejercicio 3 IV"

```
Utilizamos el comando `cde sh prueba.sh` y se nos genera el archivo cde.option y la carpeta cde-package

## Ejercicio 4

### Comprobar si el procesador o procesadores instalados tienen estos flags. ¿Qué modelo de procesador es? ¿Qué aparece como salida de esa orden?
Para ver el modelo de procesador ejecutaremos en la terminal el comando `cat /proc/cpuinfo` esto nos indica en mi caso que el procesador que monta mi ordenador es el Intel(R) Core(TM) i7-4720HQ CPU @ 2.60GHz
Tras ejecutar la orden `egrep '^flags.*(vmx|svm)' /proc/cpuinfo` vemos como no aparece ninguna línea, esto nos indica que nuestro procesador no tiene los flags activados.

## Ejercicio 5

### 1-Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden `kvm-ok` 
Primero lo tendremos que instalar con el comando `sudo apt-get install cpu-checker`, tras instalarlo podremos comprobar si el núcleo está instalado con el comando especificado `kvm-ok` y nos muestra que en mi caso concretamente no lo tiene.

### 2-Instalar un hipervisor para gestionar máquinas virtuales, que más adelante se podrá usar en pruebas y ejercicios.
He instalado vmware directamente en windows utilizando un ejecutable.
