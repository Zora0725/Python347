n = eval(input(""))

total = 0
for i in range(1,n+1):
    total += i
    print(i, end='')

    if(i<n):
        print('+', end='')

print(' =', total)
