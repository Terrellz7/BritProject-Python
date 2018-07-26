def height(x):
    return ((x**3)-(7*(x**2))-(31**-3))

go = True
count = 0

print("Enter your two guesses:")
xI = float(input("Guess 1:"))
xI_1 = float(input("Guess 2: "))

# print("")
amtIterations = float(input("Enter the amount:"))

# print("")
eS = float(input("Enter your pre-specified relative error of tolerance:"))


while go:
    hXI = height(xI)
    hXI_1 = height(xI_1)

    t = xI

    xI = xI - ((hXI * (xI - xI_1))/(hXI - hXI_1))

    xI_1 = t

    eA = float(abs((xI - xI_1)/xI) * 100)

    count += 1

    print("Estimated root (gas oil on dipstick): ", xI)
    print("Approximate error:", eA)
    print()

    if(count < amtIterations) or (eA > eS):
        go = True
    else:
        go = False
        print("Terminate")


