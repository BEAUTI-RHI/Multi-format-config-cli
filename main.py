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
        self.env_config_tokens = dict() # structure: {index: list( tuple(), str )}

    def sanitize_config(self, unsanitized_config=[]):
        if len(unsanitized_config) == 0:
            print("Error: Empty Config provided!")
            return 
        
        print("running Sanitization logic")
        print(unsanitized_config)
        
        config_keys=list()
        
        for index, var in enumerate(unsanitized_config):
            stripped = var.strip().split("=")
            print(stripped)
            env_value = stripped[1]
            

            # Save the value
            self.env_config_tokens[index] = list()
            self.env_config_tokens[index].append(env_value)

            print(self.env_config_tokens)

            # Sanitize and tokenize the key  
            # for key_token in stripped[0]:
            split_keys=stripped[0].split("_")
                    
            current_token = (self.env_config_tokens[index])
            print("--------------", "Current Token: ", current_token)
            self.env_config_tokens[index] = self.env_config_tokens[index].insert(0, tuple(split_keys))

            current_token = (self.env_config_tokens[index])
            print("========================", "Current Token: ", current_token)

        print("SANITIZATION SUCCESSFUL!")
        print(self.env_config_tokens)

    def normalize(self, configs_files):
        print("Combining config files into a master config")


    def read_config(self, configs_path=[]):
        unsanitized_config = list()
        if len(configs_path) == 0:
            print("Error: Config file required.")
            return [] 
    
        for path in configs_path:
            print("Reading config file.")
            with open(path) as file:
                unsanitized_config.append(file.readline())
        print("File read successfully")    

        return unsanitized_config


def main():
    parser = argparse.ArgumentParser(
            description="Combine multiple config files into a master file"
        )

    parser.add_argument(
            "files",
            help="Config files to process. Must be .env .toml .yaml"
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

    config_cli = Config_Cli()
    print(f"Config_files: {args.files}")
    files=[]
    files.append(args.files)

    config = config_cli.read_config(files)
    config_cli.sanitize_config(config)
    print("this is where the code will go.")
    print(f"Output path: {args.output}")
    print(f"Operation mode: {args.mode}")
    
    

if __name__ == "__main__":
    main()
