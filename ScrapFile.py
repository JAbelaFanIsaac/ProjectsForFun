monster_collection = []

class Character:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.height = 0
        self.attack = 0
        self.defence = 0

class Monster:
    def __init__(self,id,Name,Attack, Height, Intelligence,Health):
        self.id = id
        self.Name = Name
        self.Attack = Attack
        self.Height = Height
        self.Intelligence = Intelligence
        self.Health = Health

    def __repr__(self):
        return str(self.id) +" " +self.Name + str(self.Attack)

monster_collection.append(Monster(1, "elena", 300, 2, 4, 5))
print(repr(monster_collection[0]))
