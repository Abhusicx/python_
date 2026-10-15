def greet(name, location):
    print(f"Hello, {name}!")
    print(f"Welcome to {location}.")

greet("Alice", "Wonderland")

def greet(name, location="the world"):
    print(f"Hello, {name}!")
    print(f"Welcome to {location}.")

greet("Bob")