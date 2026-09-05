import math


def get_player_pos() -> tuple[float, float, float]:

    while True:
        try:
            print("Enter new coordinates as "
                  "floats in format 'x,y,z': ", end='')
            pos = input().replace(' ', '').split(',')
            if len(pos) != 3:
                raise SyntaxError
            broken = 0
            x = float(pos[0])
            broken += 1
            y = float(pos[1])
            broken += 1
            z = float(pos[2])
            break
        except SyntaxError:
            print("Invalid Syntax")
        except ValueError as error:
            print(f"Error on parameter '{pos[broken]}': {error}")
    return (x, y, z)


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:

    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


def main() -> None:

    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos = get_player_pos()
    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")
    print(f"Distance to center: {round(distance(pos, (0, 0, 0)), 4)}")
    print()
    print("Get a second set of coordinates")
    second_pos = get_player_pos()
    dist = round(distance(second_pos, pos), 4)
    print(f"Distance between the 2 sets of coordinates: {dist}")


if __name__ == "__main__":
    main()
