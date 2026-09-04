def input_temperature(temp_str: str | int) -> int:
    return int(temp_str)


def test_temperature() -> None:
    valid_input = 25
    invalid_input = "abc"
    print(f"Input data is '{valid_input}'")
    try:
        input_temperature(valid_input)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    else:
        print(f"Temperature is now {valid_input}°C")
    print()
    print(f"Input data is '{invalid_input}'")
    try:
        input_temperature(invalid_input)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    else:
        print(f"Temperature is now {invalid_input}°C")


def main() -> None:

    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
