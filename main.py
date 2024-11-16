class A:
    def __init__(self):
        print("constructor of A")
    def method(self):
        print("method of A")
    def __del__(self):
        print("destructor of A")
a1 = A()
a1.method()