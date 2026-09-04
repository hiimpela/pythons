import sys


def main() -> None:

    print("=== Player Score Analytics ===")
    scores = []
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"invalid parameter: {arg}")
    n = len(scores)
    if n == 0:
        print("No scores provided. Usage: python3", end=' ')
        print("ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {n}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / n}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
