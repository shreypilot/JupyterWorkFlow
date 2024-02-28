# same as normal function

#normal function 

def  add(a,b):
    return a+b
print(add(2,3))


#lambda function -> anonymous function -> pass into higher order function

add2 = lambda x,y: x+y
print(add2(2,3))


#Or

print((lambda x,y: x+y)(2,3))