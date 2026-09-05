import random


def gen_player_achievements() -> set[str]:
    achievements = ['Crafting Genius', 'World Savior', 'Master Explorer',
                    'Collector Supreme', 'Untouchable', 'Boss Slayer',
                    'Strategist', 'Speed Runner', 'Survivor',
                    'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder',
                    'First Steps', 'Sharp Mind']
    n = random.randint(1, len(achievements))
    return set(random.choices(achievements, k=n))


def main() -> None:

    all_achievements = set(['Crafting Genius', 'World Savior',
                            'Master Explorer', 'Collector Supreme',
                            'Untouchable', 'Boss Slayer', 'Strategist',
                            'Speed Runner', 'Survivor', 'Treasure Hunter',
                            'Unstoppable', 'Hidden Path Finder',
                            'First Steps', 'Sharp Mind'])
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    achievements = [alice, bob, charlie, dylan]
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    distinct: set[str] = set()
    for player in achievements:
        distinct = distinct.union(player)
    print(f"All distinct achievements: {distinct}")
    common = all_achievements
    for player in achievements:
        common = common.intersection(player)
    print()
    print(f"Common achievements: {common}")
    print()
    only_alice = alice.difference(bob).difference(charlie).difference(dylan)
    only_bob = bob.difference(alice).difference(charlie).difference(dylan)
    only_charlie = charlie.difference(bob).difference(alice).difference(dylan)
    only_dylan = dylan.difference(bob).difference(charlie).difference(alice)
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
