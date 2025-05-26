def bisection(f, a, b, tol):
    fa, fb = f(a), f(b)
    while fa * fb < 0 :
        c = (a + b) / 2 
        fc = f(c)
        if (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        
func = lambda x: x**3 - x - 2
root = bisection(func, 1, 2, 0.005)
print(root)