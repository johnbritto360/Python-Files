##def eveodd(num):
##    if(num%2==0):
##        print("even");
##    else:
##        print("odd");
##a=int(input());
##eveodd(a);

##def passfail(mark):
##    if(mark>=35):
##        print("Pass");
##    elif(mark<35):
##        print("Fail");
##    else:
##        print("Invalid input");
##a=int(input());
##passfail(a);

def ranger(a,b):
    for i in range(a,b):
        print(i);
a=int(input());
b=int(input());
ranger(a,b+1);
