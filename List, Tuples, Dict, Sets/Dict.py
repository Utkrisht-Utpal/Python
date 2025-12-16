# student = {
#     "name": "Utkrisht Utpal",
#     "age": 18,
#     "course": "CSE Fullstack",
#     "Skills": ["Python", "HTML", "CSS", "Javascript"],
#     "City": "Muzaffarpur"
# }

# # dictionary methods
# print(student.items())
# student.update({"age": 22, "City": "Delhi"})
# print(student.items())
# student["name"] = "Utpal Singh"
# print(student.items())

# student.pop("age")
# print(student.items())


# #print(student["marks"])  # crashes if key doesn't exist
# print(student.get("marks", "No marks")) #default value, if there is no such key


# #for printing only keys:
# for key in student:
#     print(key.title())


# #for printing only values:
# for value in student.values():
#     print(value)

# #for printing key and values:
# for key,value in student.items():
#     print(key.title(), "->" ,value)


# nested dictionaries:
# users = {
#     "u1": {"name": "Utpal", "age": 20},
#     "u2": {"name": "Amit", "age": 22}
# }
# print(users["u1"]["name"])
# print(users["u2"]["name"])

# for key,value in users.items():
#     print("---", key.title(), "---")
#     for user, info in value.items():
#         print(user.title(), "->", info)


data = {}

n = int(input("How many entries? "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print(data)