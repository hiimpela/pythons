import sys


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        print(f"[STDERR] Error opening file '{name}': {error}",
              file=sys.stderr)
        return

    print()
    try:
        print("Transform Data:")
        file = open(name, 'r')

    except OSError as error:
        print(f"[STDERR] Error opening file '{name}': {error}",
              file=sys.stderr)
        return

    new_content = [line.replace('\n', '#') for line in file]
    file.close()

    print("---")
    print()
    for line in new_content:
        print(line)
    print()
    print("---")

    print("Enter new file name (or empty): ", end='')
    sys.stdout.flush()
    new_name = sys.stdin.readline().replace('\n', '')

    if not new_name or new_name.isspace():
        print("Not saving data.")
        return

    try:
        new_file = open(new_name, 'w')

        print(f"Saving data to '{new_name}'")
        for line in new_content:
            new_file.write(line + '\n')
        new_file.close()
        print(f"Data saved in file '{new_name}'.")

    except OSError as error:
        print(f"[STDERR] Error opening file '{new_name}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return


if __name__ == "__main__":
    main()
