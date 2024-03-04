##class student:
##    def __init__(self):
##        self.name="john";
##        self.reg="1213";
##    def display(self):
##        print(self.name);
##        print(self.reg);
##s1=student();
##s2=student();
##s2.name="Naveen";
##s2.reg="103";
##s1.display();
##s2.display();

##class fruit:
##    def __init__(self,c):
##        self.color=c;
##apple=fruit("blue");
####apple.color="red";
##print(apple.color);

##class teacher:
##    def __init__(self,name,reg):
##        self.name=name;
##        self.reg=reg;
##    def display(self):
##        print(self.name);
##        print(self.reg);
##t1=teacher("John","1");
##t2=teacher("Saha","1");
##t1.display();
##t2.display();

class calc:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;
    def add(self):
        print(self.a+self.b);
    def sub(self):
        print(self.a-self.b);
    def pro(self):
        print(self.a*self.b);
    def div(self):
        print(self.a/self.b);
a=calc(19,5);
a.add();
a.sub();
a.pro();
a.div();

