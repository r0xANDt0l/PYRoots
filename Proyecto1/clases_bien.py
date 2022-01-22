class neim():
    def __init__(self, s:str, i:int, b:bool) -> None:
        self.strin = "hols"
        self.intege = 10
        self.bol = True
    def imprimir(self):
        print(self.strin,self.intege,self.bol)
    def impresion(self, algo):
        print(self.strin, algo)

class Character():
    def __init__(self, name : str) -> None:
        self.HP = 10 # Health
        self.Type = type # type of character
        self.name = name # Name of the character
        self.lvl = 10 # Level
    def get_hit(self,dmg):
        self.HP -= dmg
        if self.HP <= 0:
            self.death
    def death(self):
        print("sa matao paco")

class Player(Character):
    def __init__(self, name : str) -> None:
        super().__init__(name)
        self.inv = []
        self.gold = 10
        self.CurrXP = 1 # Current XP
    def death(self):
        self.lvl -=1
        self.HP = 10
        print("me he matao paco")


class Enemy(Character):
    def __init__(self, name : str) -> None:
        super().__init__(name)
        self.XPDrop = 10
        self.Drop = []
        self.GDrop = 0

Plyr = Player("Pedro")
# Enmy = Enemy("Zombo", "bad")

Plyr.get_hit(11)
