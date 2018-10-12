from objects.game import Game
import random

jeu = Game()

MAX = 99

while jeu.x == True:
	jeu.menu_principal()
	if jeu.choice == "1":
		# while jeu.lives > 1:
			a = random.randint(1, 9)
			b = random.randint(1, MAX)
			jeu.jeu(a, b)
	elif jeu.choice == "2":
		jeu.difficulté()
		if jeu.choice == "1":
			MAX = 9
		elif jeu.choice == "2":
			MAX = 99
		else:
			MAX = 999
	else:
		break
