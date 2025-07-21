def only_floats(a,b):
    if isinstance(a,float) and isinstance(b,float):
        return 2
    elif  isinstance(a,float) or isinstance(b,float) :
        return 1
    else:
        return 0

number=input("Enter the number separeted by comma: ").split(',')
a,b=(float(x) if '.' in x else int(x) for x in number)
result=only_floats(a, b)
print(result)