class laptop():
    ct="Type";
    def __init__(self):
        self.br="";
        self.pr=34;
    def setpr(self,pr):
        self.pr=pr;
    def getpr(self):
        print(self.pr);
    @classmethod
    def setct(cls):
        cls.ct="Type-C";
        print(cls.ct);
        
hp=laptop();
hp.setpr(40000);
hp.getpr();
laptop.setct();
