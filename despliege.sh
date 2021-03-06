#!/bin/bash

sudo apt-get update

# Instalación de vagrant
wget https://releases.hashicorp.com/vagrant/1.8.7/vagrant_1.8.7_x86_64.debsudo dpkg -i vagrant_1.8.7_x86_64.deb
# Instalar plugin para azure
vagrant plugin install vagrant-azure

# Instalación Ansible
sudo apt-get install ansible


# Despliegue en Azure
sudo vagrant up --provider=azure

# Despliegue de la aplicación con Fabric
sudo pip install fabric
# Actualiza el supervisor
fab -p '0123456789Contrasenia!' -H miguel@botmotogp.cloudapp.net demoniohup
