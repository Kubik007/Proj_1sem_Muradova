a, b, c = 7, 2, 8
def triangle_perimeter(x=a, y=b, z=c):
    return x + y + z


def triangle_area(x=a, y=b, z=c):
    return (s*(s-x)*(s-y)*(s-z))**0.5 if (s:=(x+y+z)/2) else 0