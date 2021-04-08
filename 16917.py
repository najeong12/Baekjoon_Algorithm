A, B, C, X, Y = map(int, input().split())

if A + B < 2 * C :
    price = A * X + B * Y
else :
    m = min(X, Y)
    price = A * (X-m) + B * (Y-m) + C * (2*m)
    
price = min(max(X, Y) * 2 * C, price)
print(price)