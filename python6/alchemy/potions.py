from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:

    air = create_air()
    earth = create_earth()

    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:

    fire = create_fire()
    water = create_water()

    return f"Strength potion brewed with '{fire}' and '{water}'"
