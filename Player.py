class Player:
    def __init__(self, name, minion_list):
        self.name = name
        self.minion_list = minion_list

    def addMinion(self, new_minion):
        self.minion_list.append(new_minion)
