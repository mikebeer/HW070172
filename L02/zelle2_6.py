#zelle2_6 - futval.py

def main():
   print()
   print("calc future value of investment")
   print()
   v = eval(input("initial value: "))
   r = eval(input("interest rate: "))
   y = eval(input("years: "))

   for i in range(y):
      v = v * (1+ r)
      print("{0:2d}   {1:10.2f} ".format(i+1,v))


main()
