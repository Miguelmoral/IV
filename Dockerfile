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
