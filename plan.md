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



# Here is my plan - v1.0

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


# my understanding yet: 
    this is just a case of careful text manipulation, storing them in a hash map or a list of tuples for the key value pairs.
creating a final hash map or list of key value tuples and looping over the stored texts and comparing them. we have to use a case statement for the precedence handling instead of just writing if else statements since that would become very messy.once we have looped over the entire rows of stored text list or <iterables> and psuhed then to the final list or <iterable>, we can write them to a final config file.
this should be implementation for the --resolve flag which was what the first output mode descirbed in the brief (check README.md).

The second desribed output mode in the brief is --validate. which wants us to see if the given config file matches the exact schema in the provided schema config file.

this should also be just a case of type checking. for example:
-- case 1: if the schema says :    port: integer
that means that the port key must have a value of integer. to implement this we can write a case statement that goes through the possible types of variables we can pass in the a config file i.e. Bool, integer, string, etc. and compare the required schema type for each line/property to all the possible types. when one match, we must check the same line/property in the given config file to have a value that passes the type check, for example:
-- case 1: the config file must have : port: 8080
in this case, the value 8080 is a valid integer set as the port number and therefore matches the schema provided.
if there is even a single case where the given schema is not followed by the given config file, we must throw an error and show the exact point where the sceham was not followed, what should the value be (schema) vs. what it was (config).

once all the cases are passed then the config file is valid as it matches the schema.

this is my understanding of how i should appraoch htis project. i dont know if this is gonna work or not.
