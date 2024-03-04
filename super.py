class a:
    def __init__(self):
        print("a");
    def display(self):
        print("Class a");
class b():
    def __init__(self):
        super().__init__()
        print("b");
    def display(self):
        print("Class b");

class c(b,a):
    def __init__(self):
        super().__init__()
        print("c");
    def display(self):
        print("Class c");
o=c();


