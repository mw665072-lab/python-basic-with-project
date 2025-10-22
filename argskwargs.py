

def argskwargs(*args,**kwargs):
    print(args)
    print(kwargs)

argskwargs(1,2,3,name="ahmad",age=22)


def operations(*args,**kwargs):
    sum_values =0
    for list_items in args:
        sum_values = sum_values + list_items

    print(kwargs)

    print(sum_values)

operations(1,2,3,name="waqas",age=20)

