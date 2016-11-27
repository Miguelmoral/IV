FROM ubuntu:14.04
MAINTAINER Miguel Moral Llamas <miguelmoralllamas@correo.ugr.es>
#instalamos git
RUN apt-get -y update
RUN apt-get install -y git

#Clonamos repositorio
RUN sudo git clone https://github.com/Miguelmoral/IV

#Instalamos herramientas
RUN sudo apt-get -y update
RUN sudo apt-get install -y python3-setuptools
RUN sudo apt-get -y install python3-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install3 pip
RUN sudo pip install --upgrade pip
RUN sudo pip install -r requirements.txt

ENV TOKEN="270820377:AAE8J3ISnM9LQUOl2dViqTHpRe_4w75LDW0"

CMD cd /home/iv && cd bot_motoGP && python bot.py
