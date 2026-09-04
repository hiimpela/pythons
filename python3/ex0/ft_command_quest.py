import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    n = len(sys.argv)
    if n == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {n - 1}")
    for i in range(1, n):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {n}")
    print()


if __name__ == "__main__":
    main()
