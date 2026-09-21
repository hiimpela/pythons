from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed = dark_spell_allowed_ingredients()
    words = ingredients.lower().replace(",", "").split()

    valid = any(item.lower() in words for item in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
