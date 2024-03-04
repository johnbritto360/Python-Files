d=open("fruits.txt","a");
d.write("\nHello\n");
d.write("John");
d.close();
d=open("fruits.txt","r+");
print(d.read());
