class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        if self.days <= 20:
            self.height *= 1.04
        elif self.days <= 40:
            self.height *= 1.02
        else:
            self.height *= 1.01

    def age(self) -> None:
        self.days += 1


def main() -> None:

    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    initial_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow()
        rose.show()
    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
