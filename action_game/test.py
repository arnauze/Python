from untitled.personnage import Personnage
from untitled.game import Game
import random

game = Game()
while game.x == True:
	game.menu_principal()
	if game.result == "1":
		game.start()
		break
	elif game.result == "2":
		game.shop()
	elif game.result == "3":
		game.informations()
		if game.result == "1":
			continue
		else:
			game.start()
			break
	elif game.result == "4":
		game.difficulty()
	else:
		break