import math

def func(x):
    return 2*x - math.cos(x) #Customize

first, last = 0.00, 1.00 #Customize
wanted_err = 0.001 #Customize
p = (first + last)/2
n = 1


p = (first * func(last) - last * func(first)) / (func(last) - func(first))

while (abs(func(p)) > wanted_err):
    
    p = (first * func(last) - last * func(first)) / (func(last) - func(first))
    
    if func(first) * func(p) < 0:
        last = p
    else:
        first = p

    
    print(f'{n} / {first} / {last} / {p} / {func(p)}')

    n+=1        
    