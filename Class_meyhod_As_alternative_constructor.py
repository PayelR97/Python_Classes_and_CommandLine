class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


e1 = employee("payel",22)
e1.name = "Payel"
e1.age = 22
print(e1.name)
print(e1.age)

string = "Harry-12"
e2 = employee.fromstr(string)
print(e2.name)
print(e2.age)
