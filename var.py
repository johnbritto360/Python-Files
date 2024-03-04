class phone():
    ct="Type-c";
    def __init__(self,br,pr):
        self.br=br;
        self.pr=pr;
##        self.ct="Type-c"
    def display(self):
        print(self.br);
        print(self.pr);
        print(self.ct);

##phone.ct="Lightening";
ss=phone("Samsung","40000");
ss.display();

ip=phone("iPhone","100000");
ip.display();
