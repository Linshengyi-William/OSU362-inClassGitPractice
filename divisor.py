def divisor(a):
    for i in range(1, a + 1):
        if a % i == 0:
            print(i)

inp = int(input("Enter desired number to find divisor: "))
divisor(inp)