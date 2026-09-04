class Plant:

    class _Stats:

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow,", end=' ')
            print(f"{self._age_calls} age, {self._show_calls} show")

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
        self._stats = self._Stats()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {round(self._height, 1)}cm,", end=' ')
        print(f"{self._days} days old")

    def grow(self) -> None:
        self._stats.record_grow()
        if self._days <= 20:
            self._height *= 1.08
        elif self._days <= 40:
            self._height *= 1.04
        else:
            self._height *= 1.02

    def age(self, days: int) -> None:
        self._stats.record_age()
        self._days += days

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

    @staticmethod
    def check_age(age: int) -> bool:
        return (age > 365)

    @classmethod
    def make_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):

    def __init__(self, name: str, height: float, days: int, col: str) -> None:
        super().__init__(name, height, days)
        self._color = col
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):

    _stats: '_TreeStats'

    class _TreeStats(Plant._Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(self._shade_calls, "shade")

    def __init__(self, name: str, height: float, days: int, d: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = d
        self._stats = self._TreeStats()

    def produce_shade(self) -> None:
        self._stats.record_shade()
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

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):

    def __init__(self, name: str, height: float, days: int, col: str) -> None:
        super().__init__(name, height, days, col)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


def main() -> None:

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display(rose)
    print('\n')
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display(oak)
    oak.produce_shade()
    display(oak)
    print('\n')
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display(sunflower)
    print('\n')
    print("=== Anonymous")
    anonymous = Plant.make_anonymous()
    anonymous.show()
    display(anonymous)


if __name__ == "__main__":
    main()
