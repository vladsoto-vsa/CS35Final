def main():
   values = [2,3,4,10]
   print(values)
   result = mystery(values)
   print("result: %d" % result)
   print(values)

def mystery(L):
   total = 0
   for i in range(len(L)):
      if is_odd(L[i]):
         L[i] = L[i]*2
      total = total + L[i]

   # Q2: what does the stack look like at this point?
   return total

def is_odd(number):
   # Q1: draw stack to this point (first time function is called)
   if number % 2 == 0:
      return False
   else:
      return True

main()
