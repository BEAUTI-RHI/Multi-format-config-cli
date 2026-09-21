import os
import sys

## args = sys.args

## Examples config file paths
EXAMPLE_CONFIG_TOML_PATH = 'config-examples/config.toml'
EXAMPLE_CONFIG_ENV_PATH = 'config-examples/config.env'


def parse_config_file():
    toml_hash = {}

    with open(EXAMPLE_CONFIG_TOML_PATH) as file:
        for line in file:
            # line = str(line.readline()) 
            if line[0] == '#':
                # do nothing as this line is a comment
                pass
            elif '=' in line:
                #separate the key and values and store them in a hash
                line_key_value_pair = line.split('=')
                cleaned_key = line_key_value_pair[0].strip() 
                cleaned_value = line_key_value_pair[1].strip() 

                toml_hash[cleaned_key] =  cleaned_value 
            
    print(toml_hash)

def parse_env_config_file():
    env_hash = {}

    with open(EXAMPLE_CONFIG_ENV_PATH) as file:
        for line in file:
            # line = str(line.readline()) 
            if line[0] == '#':
                # do nothing as this line is a comment
                pass
            elif '=' in line:
                #separate the key and values and store them in a hash
                line_key_value_pair = line.split('=')
                cleaned_key = line_key_value_pair[0].strip() 
                # Clean up the "" in the string values 
                cleaned_value = line_key_value_pair[1].strip() 
                if cleaned_value[0] == '"' and cleaned_value[-1] == '"':
                    unqouted_value = cleaned_value[1:-1]
                    env_hash[cleaned_key] = unqouted_value 
                else:
                    env_hash[cleaned_key] =  cleaned_value 
            
    print(env_hash)




parse_env_config_file()
