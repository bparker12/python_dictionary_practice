my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "father": {
        "name": "Ray",
        "age": 79
    }
}
# the str converts it to a string

for fam_member, details in my_family.items():
    print(f'{details["name"]} is my {fam_member} and is {str(details["age"])} years old')

# not using the age as a string

for fam_member, details in my_family.items():
    print(f'{details["name"]} is my {fam_member} and is {details["age"]} years old')


# using a comprehension

fam_stuff = {v["name"] + " is my " + k + " and is " str(v["age"]) + " years old."} for (v,k) in my_family.items()}

for member in fam_stuff:
    print(member)