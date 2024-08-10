class person:
    name = "payel"
    occupation = "data"

    def info(self):
        print(f"{self.name} is  a {self.occupation}")


s = person()
s.info()

g = person()
g.name = "harry"
g.occupation = "developer"

h = person()
h.name = "pari"
h.occupation = "accountant"

g.info()
h.info()
