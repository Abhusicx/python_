import random
print("toss!")
toss=random.randint(0,1)
if toss==0:
    print("heads")
elif toss!=0 and toss!=1:
    print("fu")
else:
    print("tails")