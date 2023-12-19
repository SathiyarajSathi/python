import random as rm
a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="0123456789"
s= "!@#$%^&*"
all = (a+A+n+s)
len = 8
password = "".join(rm.sample(all,len))
print(password)
