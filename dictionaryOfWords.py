"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
word_definitions = dict()

word_definitions["Awesome"] = "The feelinng of students when they are learninng python"

word_definitions["Cynical"] = "contemptuously distrustful of human nature and motives"

word_definitions["Apathetic"] = "having little or no interest or concern : indifferent"

print("Awesome =", word_definitions["Awesome"])
print("Cynical =", word_definitions["Cynical"])

for definition, value in word_definitions.items():
    print(f'THe definition of {definition} is {value}')


    # print(f'The definition of {definition.keys()}')