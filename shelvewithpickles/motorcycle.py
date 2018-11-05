import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "red"
    # bike["engine size"] = 250

    del bike['engin size']

    for key in bike:
        print(key)

    print(bike["engine size"])
    print(bike["colour"])
