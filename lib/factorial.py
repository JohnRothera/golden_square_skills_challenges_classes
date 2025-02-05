def factorial(n):
    product = n
    print(f"at the start product is {product}")
    while n > 1:
        n -= 1
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")

    return product


print(
    f"""
Running: factorial(8)
Expected: 40320
Actual: {factorial(8)}
"""
)
