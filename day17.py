print("\n===Table generator===")

a=int(input("enter first number="))
i=1
while(i<=10):
    print(f"{a}*{i}={a*i}")
    i+=1

import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="{}[]._!@#$"

all=lower+upper+number+symbol
length=20
password="".join(random.sample(all,length))
print(password)