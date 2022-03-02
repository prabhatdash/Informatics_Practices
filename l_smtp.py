import smtplib
import random
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('system.gen.noreply@gmail.com','apsj#123456789')
otp=random.randint(100000,999999)
message="Hello Testing SMTP from Python"+str(otp)
s.sendmail("prabhat@apsjorhat.org","6775@apsjorhat.org",message)
s.quit()
print("ENTER THE USERNAME")
name=input()
print("ENTER THE OTP")
inp_otp=int(input())
if name=='prabhat' and inp_otp==otp:
    print("LOGIN SUCCESSFUL")
else:
    print("INVALID CREDENTIALS ! PLEASE TRY AGAIN")