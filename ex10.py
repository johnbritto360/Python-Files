##class shape:
##    def area(self):
##        return 0;
##class rect(shape):
##    def area(self):
##        l=10;
##        b=12;
##        return l*b
##s1=shape();
##r=rect();
##print(r.area());
##print(s1.area());

##class person:
##    def __init__(self,name):
##        self.name=name;
##class student(person):
##    def __init__(self,name,grade):
##        super().__init__(name);
##        self.grade=grade;
##    def display(self):
##        print(self.name,self.grade);
##s=student("John","A");
##s.display();
        
##class vehicle:
##    def start(self):
##        print("Vehicle started");
##class car(vehicle):
##    def start(self):
##        print("Car started");
##c=car();
##c.start();

class emp:
    def __init__(self,name,sal):
        self.name=name;
        self.sal=sal;
class manager(emp):
    def __init__(self,name,sal,dept):
        super().__init__(name,sal);
        self.dept=dept;
    def display(self):
        print(self.name,self.sal,self.dept);
m=manager("John",20000,"cse");
m.display();
