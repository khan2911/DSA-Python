def exponential(x,n):

    if n < 0:
        raise(AttributeError("n should be positive"))

    if n ==0 :
        return 1
    element =  exponential(x,n//2)
    if n%2 == 0:
        return element *element
    else:
        return x * element * element

print(exponential(5,3))

