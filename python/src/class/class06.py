class CallableClass:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Hello, {self.name}! You called me with args: {args} and kwargs: {kwargs}")

# Create an instance of CallableClass
obj = CallableClass("John")

# Call the instance as if it were a function
obj(1, 2, 3, greeting="Hi")