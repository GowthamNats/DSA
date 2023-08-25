"""
    Abstraction:
    -----------
    Focus: Abstraction focuses on representing essential features and behavior of objects while hiding unnecessary details.
    Usage: It is achieved through abstract classes and methods, which define a contract that concrete subclasses must fulfill.
    Implementation: Abstract classes can't be instantiated directly and may contain one or more abstract methods with no implementation.
    Purpose: Abstraction simplifies complex systems by providing a clear and high-level view of their components.
    Example: Creating an abstract class "Vehicle" with abstract methods like "start_engine" and "stop_engine."

    Encapsulation:
    -------------
    Focus: Encapsulation focuses on bundling data (attributes) and methods (functions) that operate on that data into a single unit (class).
    Usage: It involves using access modifiers to control the visibility of attributes and methods outside the class.
    Implementation: Attributes can be made private (indicated by a leading underscore) to limit direct access, but access is still possible in Python.
    Purpose: Encapsulation ensures data integrity, hides the internal implementation details, and provides a clear interface for interaction.
    Example: Creating a class "Person" with private attributes like "_name" and methods to get and set the name.
"""

class Encapsulation:

    # Access modifiers => Same goes for methods too
    attribute_public = 0
    _attribute_protected = 0
    __attribute_private = 0

    def behaviour_public():
        return 0
    
    def _behaviour_protected():
        return 0
    
    def __behaviour_private():
        return 0
    
"""
    public -> can be accessed outside the class
    protected -> can be accessed by inherited classes but not outside
    private -> only inside the class
"""

"""
    Operator overloading using special methods: __<func>__ 
    Examples: __init__, __str__, __add__
"""