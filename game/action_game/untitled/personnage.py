class Personnage:
	file = open("gold.txt", "r")
	gold = int(file.read())
	file.close()
	file = open("arme.txt", "r")
	arme_lvl = int(file.read())
	file.close()
	file = open("armure.txt", "r")
	armure_lvl = int(file.read())
	file.close()
	b = 5
	l = 5
	def __init__(self, classe):
		if classe == "Archer":
			self.classe = classe
			self.life = 80 + (5 * self.armure_lvl)
			self.damages = 12 + (3 * self.arme_lvl)
			self.level = 1
			self.special = 0
		elif classe == "Mage":
			self.classe = classe
			self.life = 90 + (5 * self.armure_lvl)
			self.damages = 15 + (3 * self.arme_lvl)
			self.level = 1
			self.special = 0
		elif classe == "Guerrier":
			self.classe = classe
			self.life = 100 + (5 * self.armure_lvl)
			self.damages = 10 + (3 * self.arme_lvl)
			self.level = 1
			self.special = 0

	def takes_damages(self, user, str=""):
		if self.classe == "Guerrier" and str == "shield":
			self.life = self.life - (user.damages / 2)
		elif user.classe == "Mage" and str == "double":
			self.life = self.life - (user.damages * 2)
		else:
			self.life = self.life - user.damages

	def attack(self, user):
		user.takes_damages(self.damages)

	def level_up(self):
		if self.classe == "Archer":
			self.life += 6
			self.damages += 6
			self.level += 1
		elif self.classe == "Mage":
			self.life += 8
			self.damages += 7
			self.level += 1
		elif self.classe == "Guerrier":
			self.life += 14
			self.damages += 2
			self.level += 1

	def informations(self, gold=0, special=0):
		print("Class: {}".format(self.classe))
		print("Life: {}".format(self.life))
		print("Damages: {}".format(self.damages))
		print("Special: {}/{}".format(special, self.b))
		print("Gold: {}".format(gold))
		print("Level: {}".format(self.level))

class Boss(Personnage):
	def __init__(self, difficulty, n, classe="Boss"):
		self.classe = classe
		if ((self.l + n) % 2) == 0:
			self.l = self.l + 1
		if difficulty == "1":
			self.life = 50 + (self.l * n)
			self.hit_ratio = 5
			self.damages = 10 + (2 * n)
		elif difficulty == "2":
			self.life = 75 + (self.l * n)
			self.hit_ratio = 3
			self.damages = 13 + (3 * n)
		else:
			self.life = 100 + (self.l * n)
			self.hit_ratio = 2
			self.damages = 15 + (5 * n)

	def info(self):
		print("Class: {}".format(self.classe))
		print("Life: {}".format(self.life))
		print("Damages: {}".format(self.damages))
