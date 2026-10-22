from FortniteBot import FortniteBot

bot1 = FortniteBot("Chat")
bot2 = FortniteBot("R2-D2")
bot3 = FortniteBot("AM")

bot1.take_damage(5)
bot2.take_damage(20)

print(bot1.name)
print(bot1.health)

print(bot2.name)
print(bot2.health)

print(bot3.name)
print(bot3.health)

print("Before")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)

FortniteBot.max_health = 200

print("After")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)