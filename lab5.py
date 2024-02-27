#2
def fib(x):
    if x <= 1:
        return [1]
    else:
        lr = [1,1]
        for i in range(0,x-2):
            lr.append(lr[i]+lr[i+1])
        return lr

#O(n)
def fib_rec(n):
    if n<=1:
        return n
    else:
        fib_rec(n-1)+fib_rec(n-2)


#med bruk recursjon 2^n

print(fib(40))


#3
#en x
def a_space(n):
    z = n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):#starter
            print(' ', end='')
        for i in range(0,x):
            print('+',end='')
        for i in range(0,z):
            print(' ',end='')
        x += 2
        z -= 1
        print()

a_space(5)



