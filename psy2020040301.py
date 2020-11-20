n=int(input('number=?'))
for i in range(1,n+1,2):
    string_1='*'*i
    print(string_1 .center(n) )
for i in range(n-2,0,-2):
    string_1='*'*i
    print(string_1.center(n))