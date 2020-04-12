

def recfact(n):
    if n > 1:
        return n*recfact(n-1)
    else:
        return 1


try:
    print(recfact(900))
except (RecursionError, OverflowError):
    print("Nie można i chuj, sam se policz jak taki mądry")

print("Ende")
