lst = [1, 2, 3, 4, 5]

for i in lst:
    print(i)

x = lst[0]  # Accessing the first element
print(x)  # Output: 1

a = 0
while a < len(lst):
    x = lst[a]  # Accessing the current element
    print(x)  # Output: 1
    a += 1

dict1 = {"a": 1, "b": 2, "c": 3}
for key, value in dict1.items():
    print(key, value)

