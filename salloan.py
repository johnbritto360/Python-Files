sal=int(input("Salary: "));
age=int(input("Age: "));
if(sal>=20000 or age<=25):
    loan=int(input("Enter the loan: "));
    if(loan>=50000):
        print("Tharamudiyathu daw");
    else:
        print("You're eligible for loan");
else:
    print("You're not eligible");
