from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, element_type: str) -> None:

        self.name = name
        self.type = element_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:

        return f"{self.name} is a {self.type} type Creature"
