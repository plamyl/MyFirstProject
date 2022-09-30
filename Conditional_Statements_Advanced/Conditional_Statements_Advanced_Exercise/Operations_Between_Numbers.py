N1 = int(input())
N2 = int(input())
operator = input()
result = 0
types = ''

if operator == '+':
    result = N1 + N2
    if result % 2 == 0:
        types = 'even'
    else:
        types = 'odd'
    print(f"{N1} {operator} {N2} = {result} - {types}")

elif operator == '-':
    result = N1 - N2
    if result % 2 == 0:
        types = 'even'
    else:
        types = 'odd'
    print(f"{N1} {operator} {N2} = {result} - {types}")

elif operator == '*':
    result = N1 * N2
    if result % 2 == 0:
        types = 'even'
    else:
        types = 'odd'
    print(f"{N1} {operator} {N2} = {result} - {types}")

elif operator == '/':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")

elif operator == '%':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")


