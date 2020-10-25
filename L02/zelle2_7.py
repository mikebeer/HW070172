#zelle2_7

def main():
   print()
   print("Fixed investment plan")
   print()
   a = eval(input("Amount per year: "))
   r = eval(input("Interest rate: "))
   y = eval(input("Years: "))
   x = 0

   for i in range(y):
      x += a
      x = x * (1+r)
      print("{0:3d}  {1:10.2f}".format(i+1,x))


main()
