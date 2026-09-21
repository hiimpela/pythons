from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex0.factories import CreatureFactory
from ex2.strategy import BattleStrategy
from ex2.exception import InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    n = len(opponents)

    for i in range(n):
        for j in range(i + 1, n):
            print("* Battle *")
            first_opponent = opponents[i][0].create_base()
            second_opponent = opponents[j][0].create_base()

            print(first_opponent.describe())
            print("  vs.")
            print(second_opponent.describe())
            print("  now fight!")

            first_strategy = opponents[i][1]
            second_strategy = opponents[j][1]

            try:
                first_strategy.act(first_opponent)
                second_strategy.act(second_opponent)

            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                print()
                return
            print()


def main() -> None:

    fire_factory = FlameFactory()
    water_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    battle([(fire_factory, normal_strategy),
           (healing_factory, defensive_strategy)])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    battle([(fire_factory, aggressive_strategy),
            (healing_factory, defensive_strategy)])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    battle([(water_factory, normal_strategy),
            (healing_factory, defensive_strategy),
            (transform_factory, aggressive_strategy)])


if __name__ == "__main__":
    main()
