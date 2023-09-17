# Define a class decorator that adds a 'description' attribute to a class
def add_description(cls):
    cls.description = "This is a decorated class"
    return cls

# Apply the class decorator to a class
@add_description
class DecoratedClass:
    def __init__(self, value):
        self.value = value

# Create an instance of the decorated class
obj = DecoratedClass(42)

print(type(obj))
# Access the 'description' attribute added by the decorator
print(obj.description)  # Output: This is a decorated class
print(obj.value)
