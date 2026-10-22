class FortniteBot: #Class

    max_health = 100

    def __init__(self, bot_name): #Constructor

        self.name = bot_name #attribute
        self.health = 100 #attribute

    def take_damage(self, amount): #Method
        self.health -= amount