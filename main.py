from enemy import Troll, Enemy, Vampire, VampireKing

ugly_troll = Troll("Purg")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll - {}".format(another_troll))

brother_troll = Troll("Urg")
print(brother_troll)

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()


ugly_troll.take_damage(10)
print(ugly_troll)

dracula = Vampire("Alucard")
print(dracula)
dracula.take_damage(10)
print(dracula)

# while dracula._alive:
#     dracula.take_damage(1)
#     print(dracula)

nosf = VampireKing("Nosferatu")
print(nosf)

while nosf._alive:
    nosf.take_damage(12)
    print(nosf)
