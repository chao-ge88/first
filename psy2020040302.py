sum = 0
fac = 1
n = int(input('number=?'))
for i in range(1,n+1):
    fac *= i
    sum += fac
print(sum)