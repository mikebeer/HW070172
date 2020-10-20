# 1_7

def main():
   print("chaotic function")
   x = eval(input("Number A between 0 and 1: "))
   y = eval(input("Number B between 0 and 1: "))
   for i in range(10):
       x = 3.9 * x * (1-x)
       y = 3.9 * y * (1-y)
       print("{:.6f}".format(x) , "{:.6f}".format(y))

main()
