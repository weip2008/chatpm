# Define a class decorator
class AddPrefixToName:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, cls):
        # Define a new class that inherits from the original class
        class DecoratedClass(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.name = self.__class__.prefix + self.name

        DecoratedClass.prefix = self.prefix  # Set the prefix as a class attribute
        return DecoratedClass

# Apply the class decorator to a class
@AddPrefixToName("Prefix_")
class MyClass:
    def __init__(self, name):
        self.name = name

# Create an instance of the decorated class
obj = MyClass("Example")

# Access the instance's name attribute
print(obj.name)  # Output: Prefix_Example
