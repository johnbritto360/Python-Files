class laptop:
    def __init__(self):
        self.price=0;
        self.ram="";
        self.pro="";
    def display(self):
        print("RAM:",self.ram);
        print("Processor:",self.pro);
hp=laptop();
dell=laptop();
hp.price=10000;
hp.ram="16GB";
hp.pro="i9";
print(hp.price);
hp.display();
dell.ram="24GB";
dell.pro="i5";
dell.display();

