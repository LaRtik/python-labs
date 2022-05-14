from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path

from serializers.PicklerFactory import PicklerCreator


def convert_file(input_file_name: str, input_format: str, output_format: str) -> None:
    if input_format == output_format:
        return None
    path = Path(input_file_name)
    output_file_name = str(path.stem) + "." + output_format
    try:
        input_serializer = PicklerCreator.create(input_format)
        output_serializer = PicklerCreator.create(output_format)
    except ValueError:
        print("No serializers for " + input_format + " or " + output_format)
        exit(1)
    output_serializer.dump(input_serializer.load(input_file_name), output_file_name)


def get_args():
    parser = ArgumentParser(description="JSON/TOML/YAML converter.")
    parser.add_argument("-i", "--input", type=str, help="input file name")
    parser.add_argument("--input-format", type=str, help="input file format")
    parser.add_argument("--output-format", type=str, help="output file format")
    parser.add_argument("-c", "--config-file", type=str, help="config file")
    return parser.parse_args()


def parse_config_file(config_file_name: str) -> (str, str, str):
    config_parser = ConfigParser()
    config_parser.read(config_file_name)
    input_file_name = config_parser.get("Config", "input")
    input_format = config_parser.get("Config", "input_format")
    output_format = config_parser.get("Config", "output_format")
    return input_file_name, input_format, output_format


def parse_args(args) -> (str, str, str):
    if args.input is None:
        print("You must specify the input file name.")
        exit(1)
    if args.input_format is None:
        print("You must specify the input format.")
        exit(1)
    if args.output_format is None:
        print("You must specify the output format.")
        exit(1)
    input_file_name = args.input
    input_format = args.input_format
    output_format = args.output_format
    return input_file_name, input_format, output_format


def main() -> None:
    args = get_args()

    if args.config_file is not None:
        config_file_name = args.config_file
        input_file_name, input_format, output_format = parse_config_file(
            config_file_name
        )
    else:
        input_file_name, input_format, output_format = parse_args(args)
    convert_file(input_file_name, input_format, output_format)


if __name__ == "__main__":
    main()