def IterativeUnknown(X, Y):
    Total = 1
    while X != Y:
        print(str(X+Y))
        if X < Y:
            X = X + 1
            Total = Total * 2
        else:
            X = X - 1
            Total = int(Total/2)
    return Total

print("10 and 15")
print(IterativeUnknown(10, 15))

print("10 and 10")
print(IterativeUnknown(10, 10))

print("15 and 10")
print(IterativeUnknown(15, 10))

