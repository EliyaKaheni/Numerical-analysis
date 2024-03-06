import math

def func(x):
    return 2*x - math.sin(x) - 0.7

first, last = 0.00, 1.00
wanted_err = 0.01
p = (first + last)/2
n = 1
situation = '.'

while (abs(func(p)) > wanted_err):
    p = (first + last)/2
    
    print(f'{n} / {first} / {last} / {p} / {situation} / {func(p)}')
        
    if func(first)*func(p) > 0:
        situation = '+'
        first = p
        n+=1
        
    else:
        situation = '-'
        last = p
        n+=1
