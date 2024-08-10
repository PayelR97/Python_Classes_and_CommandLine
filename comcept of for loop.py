# Write a for loop so that every item in the list is printed.
List_1 = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for i in List_1 :
  print(i)

# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
Name = ["Lily", "Payel","Soyel","Gini","Sam","Vivek"]
for i in Name:
    print("Hello", i)

# sum of first 10 number
sum = 0
for i in range (1,11):
    sum = sum + i
print("\nThe sum of 10 nuber: ", sum)

t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)

# For loop
Fruit = ["Apple", "Orange", "Watermenlon"]
Color = ["Red", "Orange", "Green"]
for f, c in zip(Fruit, Color):
    print(f , "is", c)
