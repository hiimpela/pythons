def validate_ingredients(ingredients: str) -> str:

    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    words = ingredients.lower().replace(",", "").split()

    valid = any(item.lower() in words for item in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
