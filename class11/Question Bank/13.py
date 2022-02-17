#TO CALCULATE THE SUM OF ‘n’ NUMBER AND CHECK WHEATHER THE SUM IS EVEN OR ODD USING TRY EXCEPT.
try:
    print('enter the numbers of values')
    values=input()
    v=0
    for i in values:
        v=v+int(i)
    print("sum=",v)
except Exception as e:
    print("error",e)

