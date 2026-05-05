def func(name, age):
    return name + " " + str(age)

print(func(age= 20, name='ameeq'))


def checking_logic(*args, **kwargs):
    return args, kwargs

a, b = checking_logic(1,2, x= 2, w= 4)
print(f"args: {a} kwargs: {b}")
