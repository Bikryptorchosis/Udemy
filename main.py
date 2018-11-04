from enemy import Troll, Enemy

ugly_troll = Troll("Purg")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll - {}".format(another_troll))

brother_troll = Troll("Urg")
print(brother_troll)

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()
