import json

courses = '{"name" : "Rahulshetty", "Language": ["Java", "Python"]}'

# Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses["name"])
list = dict_courses["Language"]
print((dict_courses["Language"]))
print((dict_courses["Language"])[1])

print(len(dict_courses["Language"]))

for i in list:
    print(i, end = " ")
