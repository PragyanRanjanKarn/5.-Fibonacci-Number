x, y= 0, 1
print(x)
print(y)

n = int(input("Enter n : "))

for i in range (3, n + 1):
    z = x + y
    print(z)
    x, y = y, z