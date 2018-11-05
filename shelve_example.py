import shelve

# with shelve.open('ShelveTest') as fruit:
fruit = shelve.open('ShelveTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "cider frut"
# fruit['lemon'] = "sour bitch"
# fruit['grape'] = "tentacle grape"
# fruit['lime'] = "sour bitch don't lick"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "fuck it anyways"
#
# for snack in fruit:
#     print(snack + ': ' + fruit[snack])

# while True:
#     dict_key = input("Enter a fruta: ")
#     if dict_key == 'quit':
#         break
#
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We nota havu a " + dict_key)

# for f in sorted(fruit):
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()

# print(fruit)
