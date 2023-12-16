#Moein Moatali
"""   Tertiary equation   """

from sympy import symbols, Eq, solve

def solve_cubic_equation(a, b, c, d):
    # تعریف متغیرهای نمادین
    x = symbols('x')
    
    # تعریف معادله
    equation = Eq(a * x**3 + b * x**2 + c * x + d, 0)
    
    # حل معادله
    solutions = solve(equation, x)
    
    return solutions

# مثال برای حل معادله x^3 - 6x^2 + 11x - 6 = 0
a_val = 1
b_val = -6
c_val = 11
d_val = -6

result = solve_cubic_equation(a_val, b_val, c_val, d_val)
print(result)
