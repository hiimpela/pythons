from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.rank_counter = 0
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
            self.storage.append((self.rank_counter, str(item)))
            self.rank_counter += 1


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
            self.storage.append((self.rank_counter, item))
            self.rank_counter += 1


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
            self.storage.append((self.rank_counter, string))
            self.rank_counter += 1


class DataStream:

    def __init__(self) -> None:
        self.storage: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.storage.append(proc)

    def process_stream(self, stream: list[Any]) -> None:

        for item in stream:
            processed = False
            for proc in self.storage:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
            if not processed:
                print(f"DataStream error - Can't process element in "
                      f"stream: {item}")

    def print_processors_stats(self) -> None:

        print("== DataStream statistics ==")

        if not self.storage:

            print("No processor found, no data")
            return

        for proc in self.storage:

            if isinstance(proc, NumericProcessor):
                print("NumericProcessor: ", end='')
            elif isinstance(proc, TextProcessor):
                print("TextProcessor: ", end='')
            elif isinstance(proc, LogProcessor):
                print("LogProcessor: ", end='')

            print(f"total {proc.rank_counter} items processed, "
                  f"remaining {len(proc.storage)} on processor")


def main() -> None:

    print("=== Code Nexus - Data Stream ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()

    stream.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    stream.register_processor(NumericProcessor())
    print()

    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING', 'log_message':
              'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {batch}")

    stream.process_stream(batch)
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()

    print("Consume some elements from the data processors: Numeric 3, Text 2,"
          " Log 1")

    for i in range(3):
        stream.storage[0].output()
    for i in range(2):
        stream.storage[1].output()
    stream.storage[2].output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
