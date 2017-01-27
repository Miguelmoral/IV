from fabric.api import *

env.host = ['miguel:22']

def descargar():
    run ('sudo rm -rf IV')
    run ('sudo git clone https://github.com/Miguelmoral/IV')

def iniciar():
    run ('sudo python IV/bot_motoGP/bot.py')

def detener():
    run ('kill -9 $(pidof python)')

def borrar():
    run ('rm -rf IV')

def testear():
    run ('cd IV && make test')

def instalar():
    run ('cd IV && make install')
