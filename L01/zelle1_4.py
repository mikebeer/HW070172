# 1_4

print("chaotic function")
x = eval(input("Number between 0 and 1: "))
for i in range(20):
    x = 2.0 * x * (1-x)
    print(x)
