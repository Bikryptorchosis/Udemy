class Dupa(object):

    power_source = 'beans'

    def __init__(self, make, woof):
        self.make = make
        self.woof = woof
        self.fart = False

    def switch_on(self):
        self.fart = True


pita = Dupa("Tłuszcz", "Toxic")

print(pita.make)
print(pita.woof)

pita.woof = "Maximum toxicity"
print(pita.woof)

ann = Dupa("Miłość", "Fiołki")


print("Models: {} = {}, {} = {}".format(pita.make, pita.woof, ann.make, ann.woof))

print("Models: {0.make} = {0.woof}, {1.make} = {1.woof}".format(pita, ann))

print(pita.fart)
pita.switch_on()
print(pita.fart)

Dupa.switch_on(ann)
print(ann.fart)

print("*" * 80)

pita.powah = 2
print(pita.powah)
print(Dupa.power_source)
print(ann.power_source)
print(pita.power_source)

print(Dupa.__dict__)
print(ann.__dict__)
print(pita.__dict__)
