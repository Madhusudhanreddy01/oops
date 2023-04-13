# print("parameterized constructor--> constructor with parameter")
# class Student:
#     def __init__(self, name, roll):
#         print("Name:", name)
#         print("Rollno:", roll)

# s1=Student("madhu", 439)

print("--------------------------------------------")

print("non-parameterized constructor--> constructor with no parameter")
class Student:
    def __init__(self):
        print("Hi")
    def Info(self):
        print("Name: madhu")
        print("Rollno: 439")

s1=Student()
s1.Info()