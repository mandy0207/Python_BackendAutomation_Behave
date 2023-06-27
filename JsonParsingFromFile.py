import json

with open(r"C:\Users\msingh\PycharmProjects\pythonProject1\BackendAutomation\data.json") as reader:
    dict = json.load(reader)
    # print(dict)

dashboard_dict = dict["dashboard"]
print(dashboard_dict)
print(dashboard_dict["website"])

courseslist= dict["courses"]
print(courseslist)


print(courseslist[0])
print((courseslist[0]["title"]))
print(len(courseslist))

for course in courseslist:
    if course["title"] == "RPA":
        print(course["price"])

dict_from_list = courseslist[2]
for key in dict_from_list:
    print(key, '->', dict_from_list[key])
