"""
*Найти сумму всех четных чисел от 1 до N.
"""
n=int(input("n="))

sum=0

for i in range(1,n+1):
    if(i%2==0):
        sum+=i
print(sum)
