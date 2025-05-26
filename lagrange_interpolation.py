def lagrange_interpolate(xs, ys, x):
    """evaluate L(x) through (xs, ys) via naive O(n²) formula."""
    total = 0.0
    n = len(xs)
    for i in range(n):
        li = 1.0
        for j in range(n):
            if i != j:
                li *= (x - xs[j]) / (xs[i] - xs[j])
        total += ys[i] * li
    return total

# demo
xs = [1, 2, 4]
ys = [1, 4, 2]
print(lagrange_interpolate(xs, ys, 3))  # ≈ 3.0
