#Storing function in a list
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

operation=[add,sub,mul]#index value can be calculate the operation[0,1,2]

print(operation[0](10,20))
print(operation[1](30,20))
print(operation[2](2,20))

#Storing function in a dictionary
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

cal={
    "add:":add,
    "sub:":sub,
    "mul:":mul,
    "div:":div,
}

print(cal["add:"](10,22))
print(cal["sub:"](22,30))
print(cal["mul:"](10,2))
print(cal["div:"](11,2))