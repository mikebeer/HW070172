#zelle2_12

def main():
   print()
   print()
   print("Enter Statement. Press Enter to finish")

   while True:
      inp = input("==> ")
      if inp == "":
         break
      out = eval(inp)
      print("{0} ==> {1}".format(inp,out))
   print("END")


main()
