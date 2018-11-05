class Duck:

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Water's lovely")

    def quack(self):
        print("Quack")


class Penguin:

    def walk(self):
        print("Me waddle too, Kowalski")

    def swim(self):
        print("A lil chilly")

    def quack(self):
        print("Are ye 'avin a larf?")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)
