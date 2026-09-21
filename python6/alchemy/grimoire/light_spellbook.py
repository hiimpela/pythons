from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:

    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:

    validation_string = validate_ingredients(ingredients)

    if "INVALID" not in validation_string:
        return f"Spell recorded: {spell_name} ({validation_string})"
    return f"Spell rejected: {spell_name} ({validation_string})"
