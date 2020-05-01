x = int(input('Give me a number to count the factorial of it: '))
a = 1
for i in range(1,x+1):
    a *= i
print('The factorial of ' + str(x) + ' is: ' + str(a) + '.')
