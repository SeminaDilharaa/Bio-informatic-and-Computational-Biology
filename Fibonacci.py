fibo1,fibo2=0,1
print(fibo1,",",fibo2,end="")
f=0
for i in range(3):
    fibo3=fibo2+fibo1
    fibo1=fibo2
    fibo2=fibo3
    print(",",fibo3,end="")
print()
