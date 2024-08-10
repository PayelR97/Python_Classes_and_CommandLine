class person:

    def __init__(self, n, o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Payel", "Data analyst")
b = person("kUNAL", "fINANCE")
a.info()
b.info()


# Counting the number of objects of a class
class student:
    count = 0

    def __init__(self):
        student.count = student.count + 1


s1 = student()
s2 = student()
s3 = student()

print("the number of student is ", student.count)
