# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newvalue):
        self.value2 = newvalue

obj = ImmutableClass("Another string", 20)
print(obj.value1, obj.value2)

# attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another string"
# print(obj.value1)

# even functions within the class can't change anything
obj.some_func(5)