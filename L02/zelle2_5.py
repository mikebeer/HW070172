# zelle2_5.py
# celsius to fahrenheit

def c2f(c):
   f = 9/5 * c + 32.0
   return f

for c in range(10,101,10):
   print("{:6.2f} {:6.2f}".format(c,c2f(c)))

