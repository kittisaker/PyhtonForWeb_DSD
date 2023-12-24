def area_squre(w, h):
    result = w*h
    print(result)

area_squre(w=10, h=10)
area_squre(w=20, h=10)
area_squre(w=10, h=10)

# -------------------------------------------

def area_tri(b, h):
    result = (1/2)*b*h
    print(result)

area_tri(b=10, h=10)

# -------------------------------------------
x = lambda a: a*10
print(x(6))

y = lambda x,y: x*y
print(y(6, 6))