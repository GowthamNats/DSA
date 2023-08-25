# User defined datatype => Class
class SampleClass:
    # attributes
    attribute1 = 0
    attribute2 = 0

    # constructor
    def __init__(self):
        self.attribute1 = 50

    # behaviors / methods
    def behavior1(self):
        print("Hello World")

    def behavior2(self):
        print("Hello")

if __name__ == "__main__":
    # Instance of a class
    c = SampleClass()
    print(c.attribute1)
    c.behavior1()
