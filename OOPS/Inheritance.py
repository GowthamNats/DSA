class SuperClass:
    def __init__(self, val1, val2):
        self.attribute1 = val1
        self.attribute2 = val2

    def behavior(self):
        return self.attribute1
    
class AltClass:
    def __init__(self, val1, val2):
        self.attribute1 = val1
        self.attribute2 = val2

    def behavior4(self):
        return self.attribute1

class SubClass(SuperClass):
    def __init__(self):
        SuperClass.__init__(self, 10, 20)

    def behavior1(self):
        return self.attribute2
    
    # Using super method
    def behavior2(self):
        return super().behavior()
    
    # Method Overriding
    def behavior(self):
        return self.attribute2
    
# Multilevel Inheritance
class SubbestClass(SubClass):
    pass
    
# Multiple Inheritance
class MultiClass(SuperClass, AltClass):
    pass
""" Method Resolution Order (MRO) makes the call for the leftmost class with the corresponding method """