def main() -> None:

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    import alchemy.grimoire.dark_spellbook

    result = alchemy.grimoire.dark_spellbook.dark_spell_record(
            'boooo', 'arsenic')

    print(f"Testing record dark spell: {result}")
    print()


if __name__ == "__main__":
    main()
