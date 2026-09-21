from ex0 import FlameFactory, AquaFactory


def test_factory(factory: FlameFactory | AquaFactory) -> None:

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def fight(fire_factory: FlameFactory, water_factory: AquaFactory) -> None:

    flameling = fire_factory.create_base()
    aquabub = water_factory.create_base()

    print(flameling.describe())
    print("vs.")
    print(aquabub.describe())

    print("fight!")

    print(flameling.attack())
    print(aquabub.attack())


def main() -> None:

    fire_factory = FlameFactory()
    water_factory = AquaFactory()

    print("Testing factory")
    test_factory(fire_factory)
    print()

    print("Testing factory")
    test_factory(water_factory)
    print()

    print("Testing battle")
    fight(fire_factory, water_factory)


if __name__ == "__main__":
    main()
