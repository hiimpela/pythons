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
        print(f"{self._name}: {round(self._height, 1)}cm", end=', ')
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


def main() -> None:

    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end='')
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-6)
    rose.set_age(-7)
    print()
    print("Current state: ", end='')
    rose.show()


if __name__ == "__main__":
    main()
