from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._rank_counter = 0
        self.storage: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if type(data) is list:
            return all(type(item) in (int, float) for item in data)

        return type(data) in (int, float)

    def ingest(self, data: int | float | list[int | float]) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")

        processed_data: list[int | float] = (
            data if isinstance(data, list) else [data]
        )

        for item in processed_data:
            self.storage.append((self._rank_counter, str(item)))
            self._rank_counter += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if type(data) is list:
            return all(type(item) is str for item in data)

        return type(data) is str

    def ingest(self, data: str | list[str]) -> None:

        if not self.validate(data):
            raise ValueError("Improper text data")

        processed_data: list[str] = data if isinstance(data, list) else [data]

        for item in processed_data:
            self.storage.append((self._rank_counter, item))
            self._rank_counter += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        processed_data: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )

        if not all(type(item) is dict for item in processed_data):
            return False

        for item in processed_data:
            for key, value in item.items():
                if type(key) is not str or type(value) is not str:
                    return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:

        if not self.validate(data):
            raise ValueError("Improper log data")

        processed_data: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )

        for item in processed_data:
            string = ": ".join(item.values())
            self.storage.append((self._rank_counter, string))
            self._rank_counter += 1


def main() -> None:

    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()

    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric.ingest(numeric_data)

    print("Extracting 3 values...")
    for i in range(3):
        rank, stored_data = numeric.output()
        print(f"Numeric value {rank}: {stored_data}")

    print()
    print("Testing Text Processor...")
    text = TextProcessor()

    print(f"Trying to validate input '42': {text.validate(42)}")

    text_data: list[str] = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    text.ingest(text_data)

    print("Extracting 1 value...")
    rank, stored_data = text.output()
    print(f"Text value {rank}: {stored_data}")
    print()

    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data: list[dict[str, str]] = [
        {
            'log_level': 'NOTICE',
            'log_message': 'Connection to server'
        },
        {
            'log_level': 'ERROR',
            'log_message': 'Unauthorized access!!'
        }
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)

    print("Extracting 2 values...")
    for i in range(2):
        rank, stored_data = log.output()
        print(f"Log value {rank}: {stored_data}")


if __name__ == "__main__":
    main()
