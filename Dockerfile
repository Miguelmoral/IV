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

ENV TOKENMOTOGP="270820377:AAE8J3ISnM9LQUOl2dViqTHpRe_4w75LDW0"
ENV DATABASE_URL="postgres://duhfjfoqfomzvy:WSWZd5PeQ8wGCkIyYF-rwlFiEn@ec2-23-23-76-90.compute-1.amazonaws.com:5432/de7bsh4d838oe1"

RUN cd IV/ && make install

CMD cd /home/iv && cd bot_motoGP && python bot.py
