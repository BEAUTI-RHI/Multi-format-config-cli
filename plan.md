lets say the user types in:

multi-config-format -c config.json,config.yaml,config.toml --resolve

This should mean that the user wants us to use the three config files given as sources.
what this cli tool should be able to do is:

- merge these configs into one master config file.

what should this cli tool take care of:

same property in multiple files:

e.g: port number, GPT-API ( which could be diff in all the files ).

in this case, the file should apply a precedence structure.

1. default
2. if there is a env file, then the env should be the source of truth for the repeated prop.
3. if there is a command-line flag passed in, this should be the most authoritative.



*** Here is my plan - v1.0 ***

I think that we can open the config files. and based on the type of files, we can separate key value pairs and keep them in a hash map i.e. dict().

for example: 
in JSON:
    we know that the basic structure is:
        { "key": "value", }
in YAML:
    we know that the basic structure is:
        key: value
    this is super space sensitive so we could strip the values based on the string    method .split() and then .strip() to remove the semi colon in the key.

in TOML:
    it is the same thing as the strucutre is:
        key = 'something'
    we can basically use .split() and .strip() again for separete the values and store them in the hash map.

