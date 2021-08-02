class Minion:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health
        self.canAttack = True

    def setHealth(self, new_health):
        self.health = new_health

    def setAttack(self, new_attack):
        self.attack = new_attack

    def negateAttack(self):
        self.canAttack = not self.canAttack
