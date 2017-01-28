from fabric.api import *
import os

env.host = ['miguel:22']

def iniciar():
    with shell_env(TOKENMOTOGP=os.environ['TOKENMOTOGP'], DATABASE_URL=os.environ['DATABASE_URL']):
        run ('python IV/bot_motoGP/bot.py')

def demoniohup():
    with shell_env(TOKENMOTOGP=os.environ['TOKENMOTOGP'], DATABASE_URL=os.environ['DATABASE_URL']):
        run ('nohup python IV/bot_motoGP/bot.py >& /dev/null &',pty=False)

def descargar():
    run ('sudo rm -rf IV')
    run ('sudo git clone https://github.com/Miguelmoral/IV')

def detener():
    run ('kill -9 $(pidof python)')

def borrar():
    run ('rm -rf IV')

def testear():
    run ('cd IV && make test')

def instalar():
    run ('cd IV && make install')
