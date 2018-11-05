class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeeee")
        elif self.ratio == 1:
            print("Oof")
        else:
            print("Fak ju bicz Ima bash yo fooken ead in")


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Water's lovely")

    def quack(self):
        print("Quack")

    def fly(self):
        self._wing.fly()


class Penguin:

    def walk(self):
        print("Me waddle too, Kowalski")

    def swim(self):
        print("A lil chilly")

    def quack(self):
        print("Are ye 'avin a larf?")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # test_duck(donald)

    # percy = Penguin()
    # test_duck(percy)
