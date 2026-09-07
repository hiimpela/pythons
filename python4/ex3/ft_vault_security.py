def secure_archive(name: str, action: str = 'r',
                   content: str = '') -> tuple[bool, str]:

    if action not in ['r', 'w']:
        return (False, "Invalid action provided!")

    try:
        with open(name, action) as file:

            if action == 'w':
                file.write(content)
                return (True, "Content successfully written to file")

            return (True, file.read())

    except OSError as error:
        return (False, str(error))


def main() -> None:

    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'r'))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers", 'r'))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", 'r'))
    print()

    previous = secure_archive("ancient_fragment.txt", 'r')
    content = previous[1]
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file", 'w', content))


if __name__ == "__main__":
    main()
