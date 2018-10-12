from .personnage import Personnage, Boss
import random

class Game(object):
	x = True
	choice = "0"
	difficulty = 0
	result = 0
	file = open("gold.txt", "r")
	gold = int(file.read())
	file.close()
	file = open("arme.txt", "r")
	arme_lvl = int(file.read())
	file.close()
	file = open("armure.txt", "r")
	armure_lvl = int(file.read())
	file.close()
	upgrade_armure = (armure_lvl + 1) * 10
	upgrade_arme = (arme_lvl + 1) * 10

	def start(self, difficulty=difficulty):
		i = 0
		count = 0
		x = True
		new_gold = 0

		print("*****Welcome to the game*****\n")
		while x == True:
			print("What class would you like to pick ?")
			print("1. Archer")
			print("2. Mage")
			print("3. Guerrier")
			choice = input()

			if choice == "1":
				user = Personnage("Archer")
				break
			if choice == "2":
				user = Personnage("Mage")
				break
			if choice == "3":
				user = Personnage("Guerrier")
				break
			else:
				print("That's not a choice.\n")

		print()
		user.informations(self.gold)

		print()
		print("Ready to fight ?")
		print("Press ENTER to start.")
		input()

		while i == 0:
			print("An ennemy appeared.")
			print()

			boss = Boss(self.difficulty, count)

			boss.info()
			print()

			print("Get ready to fight.")
			print("Press ENTER to fight.")
			input()

			while i == 0:
				user.informations(self.gold)
				print()
				boss.info()
				print()

				while x == True:
					print("What do you wanna do ?")
					print("1. Attack")
					print("2. Dodge")
					choice = input()
					if choice == "1" or choice == "2":
						break

				if choice == "1":
					print("You attack the ennemy.\n")
					boss.takes_damages(user)
					if boss.life <= 0:
						print("You won the fight and earned 10 gold!")
						input();
						count = count + 1
						new_gold = new_gold + 10
						self.gold = self.gold + 10
						break
					print("Ennemy life: {}".format(boss.life))
				print("\nNow the ennemy is going to attack.")
				input()
				n = random.randint(1, boss.hit_ratio)
				if n == 2:
					print("The ennemy's attack succeeded.")
					input()
					if choice != "2":
						user.takes_damages(boss)
						print("You lost {} hp\n".format(boss.damages))
						input()
					else:
						print("But you dodged the attack.\n")
					if user.life <= 0:
						print("You're dead.\n")
						file = open("gold.txt", "w")
						file.write(str(self.gold))
						file.close()
						if count >> 1:
							print("You defeated {} bosses and recolted {} gold.".format(count, new_gold))
						elif count == 1:
							print("You defeated 1 boss and recolted 10 gold.")
						else:
							print("You lost first fight.. You suck.")
						break
				else:
					print("He missed!\n")
					input()
			if user.life <= 0:
				break
			else:
				print("You are now leveling up.\n")
				user.level_up()
				user.informations(self.gold)
				print()
				print("Continue ?")
				print("1. Yes")
				print("2. No")
				choice = input()
				if choice == "2":
					file = open("gold.txt", "w")
					file.write(str(self.gold))
					file.close()
					if count >> 1:
						print("You defeated {} bosses and recolted {} gold.".format(count, new_gold))
					elif count == 1:
						print("You defeated 1 boss and recolted 10 gold.")
					else:
						print("You lost first fight.. You suck.")
					break

	def menu_principal(self):
		self.result = 0
		while self.x == True:
			print("--------Menu principal--------")
			print("1. Commencer à jouer")
			print("2. Entrer dans le shop")
			print("3. Comment ça marche ?")
			print("4. Regler la difficulté")
			print("5. Stop game")
			self.result = input()
			if self.result == "1" or self.result == "2" or self.result == "3" or self.result == "4":
				break
			if self.result == "5":
				break
			else:
				continue

	def shop(self):
		self.result = 0
		phrase = "3. J'venais juste te faire chier"
		i = 0
		print("\nBienvenue dans le shop")
		print("Que venez-vous faire ?")
		while self.x == True:
			print("1. Améliorer mon armure")
			print("2. Améliorer mon arme")
			print("{}".format(phrase))
			self.result = input()
			if self.result == "1":
				phrase = "3. J'ai fini de te faire chier"
				print("\nTon armure est level {} et tu as {} gold".format(self.armure_lvl, self.gold))
				print("Pour améliorer ton armure il te faut {} gold\n".format(self.upgrade_armure))
				while self.x == True:
					print("Veux tu améliorer ton armure ?")
					print("1. Oui")
					print ("2. Non")
					i = input()
					if i == "1":
						if (self.gold - self.upgrade_armure) < 0:
							print("\nPas assez de gold\n")
							input()
							break
						else:
							print("\nArmure améliorée !\n")
							self.gold = self.gold - self.upgrade_armure
							file = open("gold.txt", "w")
							file.write(str(self.gold))
							file.close()
							self.upgrade_armure = self.upgrade_armure + 10
							self.armure_lvl = self.armure_lvl + 1
							file = open("armure.txt", "w").close()
							file = open("armure.txt", "w")
							file.write(str(self.armure_lvl))
							file.close()
							break
					elif i == "2":
						break
					else:
						continue
			elif self.result == "2":
				phrase = "3. J'ai fini de te faire chier"
				print("\nTon arme est level {} et tu as {} gold".format(self.arme_lvl, self.gold))
				print("Pour améliorer ton arme il te faut {} gold\n".format(self.upgrade_arme))
				while self.x == True:
					print("Veux tu améliorer ton arme ?")
					print("1. Oui")
					print ("2. Non")
					i = input()
					if i == "1":
						if (self.gold - self.upgrade_arme) < 0:
							print("\nPas assez de gold\n")
							input()
							break
						else:
							print("\nArme améliorée !\n")
							self.gold = self.gold - self.upgrade_arme
							file = open("gold.txt", "w")
							file.write(str(self.gold))
							file.close()
							self.upgrade_arme = self.upgrade_arme + 10
							self.arme_lvl = self.arme_lvl + 1
							file = open("arme.txt", "w").close()
							file = open("arme.txt", "w")
							file.write(str(self.arme_lvl))
							file.close()
							break
					elif i == "2":
						break
					else:
						continue
			elif self.result == "3":
				break
			else:
				continue

	def informations(self):
		self.result = 0
		print("=>In this game, you will impersonate a fighter. You can choose between 3 classes : Guerrier, Mage or Archer.")
		print("The Guerrier has more hp, the Mage has more damage, and the Archer is the most balanced.\n")
		print("=>You can choose between 3 levels of difficulty : Easy, Medium and Hard. In easy mode the ennemy")
		print("has 1/5 chances to touch you. In medium he has 1/3 and in hard he has 1/2.\n")
		print("=>Everytime you beat an ennemy you earn 10 gold and level up. You can then use the gold to buy upgrades")
		print("for your classes. An upgrade will increase your starting hp and damages, as well as increase the amount of increase while you level up.\n")
		while self.x == True:
			print("1. Back to menu")
			print("2. Start playing")
			self.result =input()
			if self.result == "1" or self.result == "2":
				break
			else:
				continue

	def difficulty(self):
		while self.x == True:
			print("\nChoose your difficulty:")
			print("1. Gay")
			print("2. Hetero")
			print("3. Lesbians")
			self.difficulty = input()
			if self.difficulty == "1":
				break
			elif self.difficulty == "2":
				break
			elif self.difficulty == "3":
				break
			else:
				continue
