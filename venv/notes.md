#Advance Python Arguements

## Key word Arguments
```buildoutcfg
def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
my_function(c=3, a = 1, b=2)
```
## Defualt value Arugments 
```buildoutcfg
def my_function(a=1, b=2, c=3):
    #Do this with a
    #Then do this with b
    #Finally do this with c
my_function()
0r my_function(b=5) # if I want to chage the value of the b
```
## Unlimited Positional Arguments 

```buildoutcfg
def add(*args):
    sum = 0
    for n in args:
        return sum += n
print(add(1,3,5,789))

```
## Unlimited keyword Arguments 
```buildoutcfg
def calculate(**kwargs):
    print(kwargs) # kwargs is dict with {add:3, multiply:5) 
    
print(calculate(add=3, multiply=5)
```



