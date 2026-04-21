value1 = 10;
value2 = 0;

def sum(x, y):
    return x + y;

result = (sum(value1, value2))

print(result);

def multiplication(x, y):
    return x * y;

num3 = multiplication(value1, value2);

print(num3);

def subtraction(x, y):
    return x - y;

sub = subtraction(value1, value2);

print(sub);

def division(x, y):
    if(y == 0):
        return f"ERRO! Zero division {y}";
    return x / y;

div = division(value1, value2);

print(div);