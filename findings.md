# All the things that I found while wokring on this project

1. In order to be able to validate the schema given by the user we need to check the types of each value we find in a key value pair. 

2. we can store a tuple in the hash map that we use to store the data. Basically we can store the data like this kinda : { firstKey: (value, type), }  or we could just check the type of each value on fly when we are doing the validation however it would be as robust since we can have weird value and very weird combinaions of values. I dont know if this makes sense or not but this is what is in my head for now.



- i will keep adding to this file each time i stumble upon some new idea or concept. 



## Classes Approach
    I had an idea about using classes for project and here kinda how it goes:
So first of all, we have an a class with three funditons:
`
class Config_CLI:
    def normalize():
    
    def sanitize():
    
    def read(): 
`
SO these three funcitons would do a part of the flow. Right now i understand that hte program should flow like this:

- We have n config files
- we read the config files and put them in individual data structures.
- then we use the functions to sanitize the tokens.
- then we use the fucnitons to normalize them.
- and then we compare them and create the final project using the fixed rule for precedence.

### Data Storage
    when we read a file line by line, we can store those lines in a separate data strucure for each config file.
 Then we have to sanitize the contents of each array. and we can use this structure for the list:
`
array=dict(index: list( tuple() , str))
`
So we have a hash map with the index of the line as the key and then we have the values set as a list of two elemnets:
- tuple of all the tokens of var in each line
- the value of the var as a str 
