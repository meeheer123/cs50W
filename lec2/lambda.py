people = [
    {"name" : "Harry", "house": "griffindor"},
    {"name" : "Cho", "house": "ravenclaw"},
    {"name" : "draco", "house": "slytherin"},
]


# the sort gives error since it doesnt know how to compare dict with dict
# hence we give the sort a function

# def helper(person):
#     return person["name"]


# person is the input and person["name"] is the output
people.sort(key=lambda person : person["name"])
print(people)