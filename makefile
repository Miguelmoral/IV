
install:
	sudo pip install -r requirements.txt

test:
	cd bot_motoGP && python tests.py

ejecutar:
	cd bot_MotoGP && python bot.py
