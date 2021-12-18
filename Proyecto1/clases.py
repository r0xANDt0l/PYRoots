class Plyr():
    def __init__(self) -> None:
        self.stats = [10, 10, 10, 10, 0, 10]
        self.hp = 100
        self.money = 50
        self.inv = []
    
    def ChangeMoney(self, amount : int):
        self.money += amount

player = Plyr()
player.ChangeMoney(+10)
print(player.money)