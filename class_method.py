class emp:
    company_name = "Apple"

    def show(self, name):
        print(f"The emp name is {self.name}, and comany is {self.company_name}")

    @classmethod
    def com_change(cls, newcom):
        cls.company_name = newcom


e1 = emp()
e1.name = "Harry"
e1.show("harry")
e1.com_change("Tesla")
e1.show("harry")
print(emp.company_name)
