#Moein Moatali
"""   Cubic_equation   """

import math

def cubic_equation(a: float, b: float, c: float, d: float):
    if (a == 0 and b == 0) or (a == 0):
        print("\nThis is not a cubic equation!")
        exit()

    f = ((3 * c / a) - ((b ** 2) / (a ** 2))) / 3
    g = (((2 * (b ** 3)) / (a ** 3)) - ((9 * b * c) / (a ** 2)) + (27 * d / a)) / 27
    h = (g ** 2) / 4 + (f ** 3) / 27

    if f == 0 and g == 0 and h == 0:
        if (d / a) >= 0:
            x = (d / (1 * a)) ** (1 / 3) * -1
        else:
            x = (-d / (1 * a)) ** (1 / 3)

        print("\nAll 3 roots are real and equal.")
        print("x1 = x2 = x3 =", x)

    elif h <= 0:
        i = math.sqrt(((g ** 2) / 4) - h)
        j = i ** (1 / 3)
        k = math.acos(-(g / (2 * i)))
        l = j * -1
        m = math.cos(k / 3)
        n = math.sqrt(3) * math.sin(k / 3)
        p = (b / (3 * a)) * -1

        x1 = 2 * j * math.cos(k / 3) - (b / (3 * a))
        x2 = l * (m + n) + p
        x3 = l * (m - n) + p

        print("\nAll 3 roots are real.")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)

    elif h > 0:
        r = -(g / 2) + math.sqrt(h)
        if r >= 0:
            s = r ** (1 / 3)
        else:
            s = (-r) ** (1 / 3) * -1

        t = -(g / 2) - math.sqrt(h)
        if t >= 0:
            u = (t ** (1 / 3))
        else:
            u = ((-t) ** (1 / 3)) * -1

        x1 = (s + u) - (b / (3 * a))
        x2 = -(s + u) / 2 - (b / (3 * a)) + (s - u) * math.sqrt(3) * 0.5j
        x3 = -(s + u) / 2 - (b / (3 * a)) - (s - u) * math.sqrt(3) * 0.5j

        print("\nOne real root and two complex roots.")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)