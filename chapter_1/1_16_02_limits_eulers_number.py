from sympy import symbols, limit, oo, plot

n = symbols('n')
f = (1 + (1/n))**n
result = limit(f, n, oo)

print(result)  # E
print(result.evalf())  # 2.71828182845905
plot(f, (n, 0, 10))
