##class comp:
##    def __init__(self):
##        self._name="Google";
##    def cmpname(self):
##        print(self.__name);
##c=comp();
##print(c._name);

class comp:
    def __init__(self):
        self._name="Google";
class b(comp):
    pass
b1=b();
print(b1._name);
