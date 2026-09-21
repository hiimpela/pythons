from abc import ABC, abstractmethod
from ex0.creature import Creature
from .exception import InvalidStrategyError
from ex1.capabilities import HealCapability, TransformCapability
from typing import Any


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Any) -> None:

        if not self.is_valid(creature):

            message = f"Invalid object: '{creature.name}' is not a Creature"
            raise InvalidStrategyError(message)
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Any) -> None:

        if not self.is_valid(creature):

            message = (
                    f"Invalid Creature '{creature.name}' for this "
                    f"aggressive strategy"
            )
            raise InvalidStrategyError(message)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Any) -> None:

        if not self.is_valid(creature):

            message = (
                    f"Invalid Creature '{creature.name}' for this "
                    f"defensive strategy"
            )
            raise InvalidStrategyError(message)
        print(creature.attack())
        print(creature.heal())
