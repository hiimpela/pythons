

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


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin():

    def process_output(self, data: list[tuple[int, str]]) -> None:

        output_string = ""
        for item in data:
            output_string += item[1] + ','

        print(output_string[:-1])


class JSONPlugin():

    def process_output(self, data: list[tuple[int, str]]) -> None:

        output_string = '{'
        for item in data:
            output_string += '"item_' + str(item[0]) + '": "' + item[1] + '", '
        print(output_string[:-2] + '}')


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        for proc in self.storage:
            output_list = []
            counter = 0
            if type(plugin) is CSVPlugin:
                print("CSV output: ")
            else:
                print("JSON output: ")

            while proc.storage and counter < nb:
                output_list.append(proc.output())
                counter += 1

            plugin.process_output(output_list)


def main() -> None:

    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()
    print()

    stream.print_processors_stats()
    print()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    first_batch = ['Hello world', [3.14, -1, 2.71],
                   [{'log_level': 'WARNING', 'log_message':
                    'Telnet access! Use ssh instead'},
                    {'log_level': 'INFO', 'log_message':
                    'User wil is connected'}], 42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    print()

    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_exporter = CSVPlugin()
    stream.output_pipeline(3, csv_exporter)

    stream.print_processors_stats()
    print()

    second_batch = [21,
                    ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                    [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                     {'log_level': 'NOTICE', 'log_message':
                        'Certificate expires in 10 days'}],
                    [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"Send another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    print()

    stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_exporter = JSONPlugin()

    stream.output_pipeline(5, json_exporter)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
