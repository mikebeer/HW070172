# zelle2_3b

def main():
  print("avg of n values")
  data = input("input values separated by comma")
  data = "["+data+"]"
  list = eval(data)
  print(list)

  s   = sum(list)
  l   = len(list)

  avg = s/l
  print("average = ",avg)

main()
