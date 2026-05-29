

## 1. Print all even numbers from 1 to 100

#for i in range(2, 101, 2):
 #   print(i)

## 2. Print numbers from 50 to 1 in reverse

#for i in range(50, 0, -1):
    # print(i)
#print ()

## 3. Sum of first 50 natural numbers

#sum = 0

#for i in range(1, 51):
 #   sum = sum + i

#print("Sum =", sum)


## 4. Multiplication tables from 1 to 10


#   print("Table of", i)

   # for j in range(1, 11):
    #    print(i, "x", j, "=", i * j)

    #print()



## 5. Count digits in a number

#num = int(input("Enter a number: "))

#count = 0

#while num > 0:
 #   num = num // 10
  #  count += 1

#print("Total digits =", count)


## 6. Factorial of a number

#num = int(input("Enter a number: "))

#fact = 1

#for i in range(1, num + 1):
 #   fact = fact * i

#print("Factorial =", fact)


## 7. Print all odd numbers from 1 to 100

#for i in range(1, 101, 2):
 #   print(i)


## 8. Star square pattern

#rows = 5

#for i in range(rows):
 #   for j in range(rows):
  #      print("*", end=" ")
   # print()


## 9. Check whether a number is prime

#num = int(input("Enter a number: "))

#is_prime = True

#if num <= 1:
 # for i in range(2, num):
  #      if num % i == 0:
   #         is_prime = False
    #break

#if is_prime:
 #   print("Prime Number")
#else:
 #   print("Not Prime Number")


## 10. Fibonacci series up to 15 terms

#a = 0
#b = 1

#print(a)
#print(b)

#for i in range(13):
 #   c = a + b
  #  print(c)

   # a = b
    #b = c


## 11. Numbers divisible by both 3 and 5

#for i in range(1, 101):
 #   if i % 3 == 0 and i % 5 == 0:
  #      print(i)


## 12. Reverse a number using while loop

#num = int(input("Enter a number: "))

#reverse = 0

#while num > 0:
 #   digit = num % 10
  #  reverse = reverse * 10 + digit
   # num = num // 10

#print("Reversed Number =", reverse)


## 13. Sum of digits of a number

#num = int(input("Enter a number: "))

#sum = 0

#while num > 0:
 #   digit = num % 10
  #  sum = sum + digit
   # num = num // 10

#print("Sum of digits =", sum)


## 14. Pattern printing


#for i in range(1, 6):
 #   print("*" * i)


## 15. Print ASCII values from A to Z

#for i in range(65, 91):
 #   print(chr(i), "=", i)


## 16. Right-angle triangle using numbers

#for i in range(1, 6):
 #   for j in range(1, i + 1):
  #      print(j, end=" ")
   # print()


## 17. Ask user input until "exit"

#while True:
 #   text = input("Enter something: ")

  #  if text == "exit":
 #       break

  #  print("You entered:", text)


## 18. Countdown timer

#num = int(input("Enter countdown number: "))

#while num > 0:
 #   print(num)
  #  num -= 1

#print("Time's up!")



## 19. Print all prime numbers between 1 and 200
#for num in range(2, 201):

 #   is_prime = True

  #  for i in range(2, num):
   #     if num % i == 0:
    #        is_prime = False
    #      break

    #if is_prime:
     #   print(num)
## 20. Pyramid pattern program
rows = 5
# for i in range(1 rows + 1);
# print ("*"* i)

#for i in range(rows,0,-1): print(("1,2,3,4,5"))
rows = 5

for i in range( rows +1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



