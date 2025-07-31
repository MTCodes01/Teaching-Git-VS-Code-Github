# print("Hi", "there!")
# print("Hi", "there!", sep=", ")
# print("Hi", "there!", end=".")
# print("Hi", "there!", sep=", ", end=".")
# print("Hi", "there!", file=open("output.txt", "w"))

# def func1(a: int, b: int) -> int:
#     """Returns the sum of two integers."""
#     return a + b

# func1 = lambda a, b: a+b
# print(func1(1, 2))
# print(func1(12, 45))

lst1 = [1, 2, 3, 4, 5]
# for i in range(0, 10):
#     lst1.append(i)

# lst2 = [i for i in range(0, 10)]

dict1 = {i:j for i,j in enumerate(lst1, start=5)}

# print(list(enumerate(lst1, start=5)))
# print(f"List 1: {lst1}\nList 2: {lst2}")
print(dict1)