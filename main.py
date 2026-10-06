import os
import sys
import argparse

## args = sys.args

## Examples config file paths
EXAMPLE_CONFIG_TOML_PATH = 'config-examples/config.toml'
EXAMPLE_CONFIG_ENV_PATH = 'config-examples/config.env'
class Config_Cli():
    def __init__(self, mode="combine", output_path="./"):
        self.output_path = output_path
        self.operation_mode = mode

    def validate_config_schema(self, schema, config_file):
        print("Validating config against the schema")

    def combine_config_sources(self, configs_files):
        print("Combining config files into a master config")


def main():
    parser = argparse.ArgumentParser(
            description="Combine multiple config files into a master file"
        )

    parser.add_argument(
            "-o", "--output",
            type=str,
            default="./",
            help="The path for the output file"
        )
    parser.add_argument(
            "-m", "--mode",
            type=str,
            default="c",
            help="The operation to do on the input files."
        )
    
    args = parser.parse_args()

    print("this is where the code will go.")
    print(f"Output path: {args.output}")
    print(f"Operation mode: {args.mode}")
    
    

if __name__ == "__main__":
    main()
