import random


def main() -> None:

    print("=== Command Quest ===")
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
             'kevin', 'Liam']
    all_capitalized = [name.capitalize() for name in names]
    capitalized_only = [name for name in names if name == name.capitalize()]

    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {capitalized_only}")
    print()

    scores = {name: random.randint(1, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    score_average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {score_average}")

    high_scores = {key: value for key, value in scores.items()
                   if value > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
