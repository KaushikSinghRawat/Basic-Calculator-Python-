for i in range (1, 100):
   com1 = i%3
   com2 = i%5
   if com1 == 0 and com2 == 0:
      print("FizzBuzz")
   elif com1 == 0:
      print("Fizz")
   elif com2 == 0:
      print("Buzz")
   else:
      print(i)
