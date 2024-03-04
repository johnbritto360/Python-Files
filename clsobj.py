class goa:
    name="john";
    drink="";
    def party(self):
        print("Lets party");
    def beach(self):
        print("Lets Enjoy");
g=goa();
o=goa();
g.party();
g.beach();
o.beach();
print(o.name);
g.name="saha";
print(o.name);
print(g.name);
o.name="messi";
print(o.name);
g.drink="Yes";
o.drink="No";
print(g.drink);
print(o.drink);
