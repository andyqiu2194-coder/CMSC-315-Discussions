"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "Parent"

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display_info(self):
        return f"Name: {self.name}, Value: {self.value}, Category: {self.category}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    category = "Child"

    def __init__(self, name, value, grade, courses):
        super().__init__(name, value)
        self.grade = grade
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)

    def display_info(self):
        return (
            f"Name: {self.name}, Value: {self.value}, "
            f"Grade: {self.grade}, Courses: {self.courses}, "
            f"Category: {self.category}"
        )

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass(
        "Alice",
        100,
        "A",
        ["CMSC 315"]
    )

    student2 = ChildClass(
        "Bob",
        85,
        "B",
        ["CMSC 315", "MATH 141"]
    )

    print("Class variable through class:", ChildClass.category)
    print("Class variable through student1:", student1.category)
    print("Class variable through student2:", student2.category)

    # Add an attribute only to student1.
    student1.favorite_subject = "Computer Science"

    print("\nStudent 1 namespace:")
    print(student1.__dict__)

    print("\nStudent 2 namespace:")
    print(student2.__dict__)

    print("\nChildClass namespace:")
    print(ChildClass.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Charlie",
        90,
        "A",
        ["CMSC 315", "CMSC 330"]
    )

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new outer object, but nested mutable
    # objects, such as the courses list, are still shared.
    #
    # A deep copy creates a new outer object and independent copies
    # of nested mutable objects.

    original.courses.append("CMSC 350")

    print("Original:")
    print(original.display_info())

    print("\nShallow copy:")
    print(shallow_copy.display_info())

    print("\nDeep copy:")
    print(deep_copy.display_info())


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nParent object:")
    parent = ParentClass("David", 75)
    print(parent.display_info())

    print("\nChild object:")
    child = ChildClass(
        "Emma",
        95,
        "A",
        ["CMSC 315"]
    )
    print(child.display_info())

    print("\nAdding a course to child object:")
    child.add_course("CMSC 330")
    print(child.display_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
