##try:
##    a=int(input());
##    b=int(input());
##    print(a+b);
##except Exception as e:
##    print(e);

try:
    a=int(input());
    b=int(input());
    c=input();
    print(b/a);
    print(d);
except ValueError as e:
    print(e);
except TypeError as e:
    print(e);
except NameError as e:
    print(e);
finally:
    print("Done");
