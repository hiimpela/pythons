def input_temperature(temp_str: str | int) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    elif temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
    valid_input = 25
    input_string = "abc"
    input_too_hot = 100
    input_too_cold = -50

    print(f"Input data is '{valid_input}'")
    try:
        input_temperature(valid_input)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    else:
        print(f"Temperature is now {valid_input}°C")
    print()
    print(f"Input data is '{input_string}'")
    try:
        input_temperature(input_string)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    else:
        print(f"Temperature is now {input_string}°C")
    print()
    print(f"Input data is '{input_too_hot}'")
    try:
        input_temperature(input_too_hot)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    else:
        print(f"Temperature is now {input_too_hot}°C")
    print()
    print(f"Input data is '{input_too_cold}'")
    try:
        input_temperature(input_too_cold)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    else:
        print(f"Temperature is now {input_too_cold}°C")


def main() -> None:

    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
