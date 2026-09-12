from alchemy.potions import healing_potion, strength_potion


def main() -> None:

    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(healing_potion())
    print(strength_potion())
    print()


if __name__ == "__main__":
    main()
