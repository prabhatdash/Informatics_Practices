# a=60
# b=50
#
# while True:
#     q=a//b
#     r=a%b
#     if r==0:
#         print(b)
#         break
#     else:
#         a=b
#         b=r

year=int(input("enter the year"))
if ((year%4==0) and (not (year%100==0))) or (year%400==0):
    print("Leap Year")


