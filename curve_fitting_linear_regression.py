import numpy as np
from numpy import polyfit

x = np.array([1,2,3,4])
y = np.array([2.2, 2.8, 3.6, 4.5])

a,b = polyfit(x, y, 1)

print(f"Doğru denklemi: y = {a:.2f}x + {b:.2f}")

#real implementation of linear regression 

def linear_regression(x, y):
    #y = m x + b
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = sum(xi*xi for xi in x)
    sxy = sum(xi*yi for xi, yi in zip(x,y))

    denom = n * sxx - sx * sx
    if denom == 0:
        raise ValueError("Slope yok!")
    m = (n * sxy - sx * sy) / denom
    b =  (sy - m * sx) / n
    return m, b

m, b = linear_regression(x, y)
print(f"Polyfit kullanmadan: y = {m:.3f} x + {b:.3f}")
