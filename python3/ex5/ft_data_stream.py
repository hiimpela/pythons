import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim',
               'release', 'use']

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple[str, str]]) -> \
        typing.Generator[tuple[str, str], None, None]:

    while len(events):
        pick = random.choice(events)
        events.remove(pick)
        yield pick


def main() -> None:

    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        (player, action) = next(gen_event())
        print(f"Event {i}: Player {player} did action {action}")

    events = [next(gen_event()) for i in range(10)]
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print()
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
