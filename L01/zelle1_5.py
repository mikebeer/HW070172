# 1_5

print("chaotic function")
x = eval(input("Number between 0 and 1: "))
n = eval(input("how often? "))
for i in range(n):
    x = 3.9 * x * (1-x)
    print(x)
