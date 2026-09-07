import sys


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    name = sys.argv[1]

    try:
        print(f"Accessing file '{name}'")
        file = open(name, 'r')

        print("---")
        print()
        print(file.read())
        print()
        print("---")

        file.close()
        print(f"File '{name}' closed.")

    except OSError as error:
        print(f"Error opening file '{name}': {error}")


if __name__ == "__main__":
    main()
