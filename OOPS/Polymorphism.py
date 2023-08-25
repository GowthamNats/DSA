class Class:
    def behavior(self):
        print("Class 1")

class Class1(Class):
    def behavior(self):
        print("Class 2")

class Class2(Class):
    def behavior(self):
        print("Class 3")

if __name__ == "__main__":
    c1 = Class1()
    c1.render()

    c2 = Class2()
    c2.render()
