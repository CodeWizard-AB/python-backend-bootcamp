"""
Python Functions — Examples

Heavily commented so this file works as a second set of notes,
not just runnable code.
"""

# --- 1. Basic function definition -------------------------------------
def greet(name):
    """A function is a reusable block of code — like a labeled recipe
    you can call by name instead of rewriting the steps every time."""
    return f"Hello, {name}!"

print(greet("Anunay"))  # -> Hello, Anunay!


# --- 2. Default arguments ------------------------------------------------
def greet_with_default(name="stranger"):
    # If no argument is passed, "stranger" is used automatically.
    return f"Hello, {name}!"

print(greet_with_default())        # -> Hello, stranger!
print(greet_with_default("Argha")) # -> Hello, Argha!


# --- 3. *args and **kwargs -----------------------------------------------
def add_all(*numbers):
    # *numbers collects any number of positional arguments into a tuple.
    # Think of it as a variable-sized box that can hold as many items
    # as the caller wants to hand over.
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # -> 10


def show_profile(**details):
    # **details collects keyword arguments into a dictionary.
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Anunay", role="Full Stack Developer")


# --- 4. Return values vs side effects -------------------------------------
def add(a, b):
    # This function RETURNS a value — the caller decides what to do with it.
    return a + b

def print_sum(a, b):
    # This function has a SIDE EFFECT (printing) but returns nothing (None).
    print(a + b)

result = add(2, 3)      # result = 5, usable later
print_sum(2, 3)         # prints 5, but nothing is stored


# --- 5. Lambda (anonymous) functions --------------------------------------
# Useful for short, throwaway functions — e.g. as a sort key.
square = lambda x: x * x
print(square(5))  # -> 25

numbers = [4, 1, 3, 2]
numbers.sort(key=lambda x: -x)  # sort descending
print(numbers)  # -> [4, 3, 2, 1]
