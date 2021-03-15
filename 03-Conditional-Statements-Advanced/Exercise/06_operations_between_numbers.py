n1 = int(input())
n2 = int(input())
operation = input()

result = 0
even_or_odd = ""

if operation == "+":
    result = n1 + n2
elif operation == "-":
    result = n1 - n2
elif operation == "*":
    result = n1 * n2

if result % 2 == 0:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

if n2 == 0 and (operation == "/" or operation == "%"):
    print(f"Cannot divide {n1} by zero")
elif operation == "/":
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")
elif operation == "%":
    result = n1 % n2
    print(f'{n1} % {n2} = {result}')

if operation == "+" or operation == "-" or operation == "*":
    print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")






