def print_params(a = 1,b = "строка",c = True):
    print(a,b,c)
print_params()
print_params(10,"Арбуз", False)

values_list=[100,"Урбан",True]
values_dick={"a": 0, "b":"Юнити","c": False}

print_params(*values_list)
print_params(**values_dick)

values_list_2=[-12,True]
print_params(*values_list_2, 42)