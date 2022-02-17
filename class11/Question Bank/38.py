#to find simple and compound interest
p=float(input("PRINCIPAL AMOUNT:"))
r=float(input("RATE OF INTEREST:"))
t=float(input("TIME:"))
n=float(input("number of times interest applied"))
PI=(p*r*t)/100
print("PRINCIPAL INTETEST:",PI)
Ci=p(1+(r/n))**3
print("COMPOUND INTEREST:",Ci)