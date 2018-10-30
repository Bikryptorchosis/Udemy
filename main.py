from player import Player

pita = Player("Pita")

print(pita.name)
print(pita.lives)

pita.lives -= 1
print(pita)
pita.lives -= 1
print(pita)
pita.lives -= 1
print(pita)
pita.lives -= 1
print(pita)
pita.lives -= 1
print(pita)

pita.lives += 1
print(pita)
pita.level += 1
print(pita)
pita.level = 10
print(pita)
pita.level = 5
print(pita)
pita.level = 0
print(pita)

pita.score = 500
print(pita)
