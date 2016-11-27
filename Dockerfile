FROM ubuntu:16.04
MAINTAINER Miguel Moral Llamas <miguelmoralllamas@correo.ugr.es>
#instalamos git
RUN apt-get -y update
RUN apt-get install -y git

#Clonamos repositorio
RUN sudo git clone https://github.com/Miguelmoral/IV

#Instalamos herramientas
RUN sudo apt-get -y update
RUN sudo apt-get install python2.7
RUN sudo apt-get install -y python-pip
RUN sudo apt-get install -y python-software-properties
RUN sudo apt-get install -y build-essential
RUN sudo apt-get install -y libpq-dev
RUN sudo apt-get install -y libxml2-dev libxslt-dev  python-dev  python-setuptools
RUN sudo pip install -r requirements.txt

ENV TOKEN="270820377:AAE8J3ISnM9LQUOl2dViqTHpRe_4w75LDW0"

CMD cd /home/iv && cd bot_motoGP && python bot.py
