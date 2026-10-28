# Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

# For Henry Davids, the output should be:

# Mr. Henry Davids
# For Mary George, the output should be:

# Ms. Mary George
# Input Format

# The first line contains the integer , the number of people.
#  lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

# Constraints


# Output Format

# Output  names on separate lines in the format described above in ascending order of age.

# Sample Input

# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F
# Sample Output

# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle

from __future__ import annotations
from enum import Enum

class Sex(Enum):
    MALE = 'M'
    FEMALE = 'F'

class Prefix(Enum):
    MR = 'Mr.'
    MS = 'Ms.'

class ProgramError(Exception):
    def __init__(self, message):
        self.message = message

class Person:
    def __init__(self, first_name: str, last_name: str, age: int, sex: Sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.sex = sex

def order_by_age(f):
    def inner(people: list[Person]) -> list[str]:
        # 1. Sort the list using the decorator logic
        sorted_people = sorted(people, key=lambda x: x.age)
        # 2. Pass the sorted list to the original function
        return f(sorted_people)
    return inner

@order_by_age
def print_full_name(people: list[Person]) -> list[str]:
    result = []
    for person in people:
        if person.sex is None:
            raise ProgramError("Sex is not defined")

        if person.sex == Sex.MALE:
            result.append(f"{Prefix.MR.value} {person.first_name} {person.last_name}")
        elif person.sex == Sex.FEMALE:
            result.append(f"{Prefix.MS.value} {person.first_name} {person.last_name}")
        else:
            raise ProgramError("Invalid sex value")
            
    return result

if __name__ == "__main__":
    print("Starting the program...")

    mike = Person("Mike", "Thomson", 20, Sex.MALE)
    robert = Person("Robert", "Bustle", 32, Sex.MALE)
    andria = Person("Andria", "Bustle", 30, Sex.FEMALE)

    people = [mike, robert, andria]

    # This invokes the decorator (sorting) -> then invokes print_full_name (formatting)
    result = print_full_name(people)

    for r in result:
        print(r)
    
    print('Program finished.')
