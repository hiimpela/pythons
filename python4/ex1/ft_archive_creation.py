import sys


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

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

    print()
    try:
        print("Transform Data:")
        file = open(name, 'r')

    except OSError as error:
        print(f"Error opening file '{name}': {error}")
        return

    new_content = [line.rstrip('\n') + '#' for line in file]
    file.close()

    print("---")
    print()
    for line in new_content:
        print(line)
    print()
    print("---")

    new_name = input("Enter new file name (or empty): ")
    if not new_name or new_name.isspace():
        print("Not saving data.")
    else:
        try:
            new_file = open(new_name, 'w')

            print(f"Saving data to '{new_name}'")
            for line in new_content:
                new_file.write(line + '\n')
            new_file.close()
            print(f"Data saved in file '{new_name}'.")

        except OSError as error:
            print(f"Error opening file '{new_name}': {error}")


if __name__ == "__main__":
    main()
