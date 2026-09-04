class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        if days < 0:
            self._days = 0
            print("Age can't be negative, defaulted to 0")
        else:
            self._days = days
        if height < 0:
            self._height = 0.0
            print("Height can't be negative, defaulted to 0")
        else:
            self._height = height

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,", end=' ')
        print(f"{self._days} days old")

    def grow(self) -> None:
        if self._days <= 20:
            self._height *= 1.04
        elif self._days <= 40:
            self._height *= 1.02
        else:
            self._height *= 1.01

    def age(self) -> None:
        self._days += 1
        self.grow()

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}:", end=' ')
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._days = new_age
            print(f"Age updated: {self._days} days")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}:", end=' ')
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_age(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height


class Flower(Plant):

    def __init__(self, name: str, height: float, days: int, col: str) -> None:
        super().__init__(name, height, days)
        self._color = col
        self._bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name: str, height: float, days: int, d: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = d

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of", end=' ')
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, days: int, mnth: str) -> None:
        super().__init__(name, height, days)
        self._harvest_season = mnth
        self._nutritional_value = 0

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print('\n')
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print('\n')
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
