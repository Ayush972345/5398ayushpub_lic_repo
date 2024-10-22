class MyClass:
    def __init__(self, **kwargs):
        # Accessing kwargs
        self.name = kwargs.get('name', 'Unknown')
        self.age = kwargs.get('age', 0)

        # Updating kwargs (adding a new key-value pair)
        kwargs['location'] = 'Unknown Location'

        # Store the updated kwargs in an attribute for future use
        self.kwargs = kwargs

    def update_kwargs(self, **new_kwargs):
        # Update the existing kwargs with new values
        self.kwargs.update(new_kwargs)

    def display_info(self):
        # Access and display the kwargs content
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.kwargs.get('location', 'No Location')}")
        # Print all kwargs
        print("Full kwargs:", self.kwargs)


# Create an instance of MyClass
person = MyClass(name="John", age=30)

# Access and display the kwargs
person.display_info()

# Update kwargs
person.update_kwargs(location="New York", job="Developer")

# Display the updated info
person.display_info()

