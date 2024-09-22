def fun():
    x = float(input('enter the first number'))
    y = float(input('enter the second number'))
    return x+y
num=fun()
print(num)
def prime(num):
    if num<=3:
        return 'prime'
    if num<=0:
        return ' 0 or -ve numbers are not prime'
    else:
        for i in range(2,num):
            if num% i ==0:
                return 'not prime'
    return 'prime'
print(prime(num))
    

