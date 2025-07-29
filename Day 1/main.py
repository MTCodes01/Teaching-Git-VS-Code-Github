def func1(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

print(func1(3, 5))  # Output: 8

print("Hi", "there!")
print("Hi", "there!", sep=", ")
print("Hi", "there!", end=".")
print("Hi", "there!", sep=", ", end=".")
print("Hi", "there!", file=open("output.txt", "w"))

class ClassA:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func1(self):
        """Returns the sum of two integers."""
        return self.a + self.b
    
if __name__ == "__main__":
    obj = ClassA(3, 5)
    print(obj.func1())