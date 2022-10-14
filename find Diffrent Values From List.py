list1 = []
list2 = []

x = int(input("Input list1 lenght: "))

for i in range(0, x):
    nilai1 = int(input("Input list1 values: "))
    list1.append(nilai1)

y = int(input("Input list2 lenght: "))

for i in range(0, y):
    nilai2 = int(input("Input list2 values: "))
    list2.append(nilai2)

duplicate = set(list1) & set(list2)
print("Same values:", duplicate)
