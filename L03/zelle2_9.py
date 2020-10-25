#zelle2_9

def f2c(f):
   c= 5*(f-32)/9
   return c


def main():
   print("Fahrenheit to Celsius")
   x = eval(input("f"))
   print(x,f2c(x))

main()
