# Examplen1
#name = "Vartika"
#age = 21
#gpa = 3.75
#print ('name:', name , 'age:', age , 'gpa:', gpa)
 # Example 2
#x = 10
#x = 20
#a , b , c = 1 , "2" , 3
#print(a , b , c)
# Example 3
#print (4 ** 2)
#print (3 * 4)
#print (2 + 3)
#print (2 - 1)
# Example 4 
#x = 10 
#print (x == 10)
#print (x !=5 )
#print (x > 15)
#print (x <= 10)
# Example 5

# table_of = 9
# print(f"\nTable of {table_of} (1 to 12):")
# for i in range(1, 13):
#      print(f"  {table_of}  X {i:2} = {table_of * i:3}")
#print("\n5x5 Multiplication Table:")
#print("    ", end="")
#for col in range(1, 6):
 #   print(f"{col:4}", end="")
#print()
#print("   " + "-" * 21)
#   print(f"{row:2} |", end="")
 #   for col in range(1, 6):
  #      print(f"{row * col:4}", end="")
   # print()
# Assingment 1 

# Q1. Positive, Negative, or Zero

#num = float(input("Enter a number: "))

#if num > 0:
#print("Positive") 
 #elif num < 0:
    #print("Negative")
#else:
 #   print("Zero")

# Q2. Greater Number or Equal

#a = float(input("Enter first number: "))
#b = float(input("Enter second number: "))

#if a > b:
 #   print(a, "is greater")
#elif b > a:
 #   print(b, "is greater")
#else:
 #   print("Both are equal")

    # Q3. Leap Year Check

#year = int(input("Enter a year: "))

#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 #   print("Leap Year")
#else:
 #   print("Not a Leap Year")

# Q4. Print Odd Numbers from 1 to 50

#for i in range(1, 51, 2):
 #   print(i)

# Q5. Password Checker

#password = ""

#while password != "python123":
 #   password = input("Enter password: ")

#print("Access Granted!")

# Q6. Multiplication Table

#num = int(input("Enter a number: "))

#for i in range(1, 11):
 #   print(num, "x", i, "=", num * i)

# Q7. Sum from 1 to 100

#total = 0

#for i in range(1, 101):
 #   total += i

#print("Sum =", total)

# Q8. Factors of a Number

#num = int(input("Enter a number: "))

#print("Factors are:")

#for i in range(1, num + 1):
 #   if num % i == 0:
  #      print(i)

# Q9. Star Pattern

#for i in range(1, 6):
 #   for j in range(i):
    #    print("*", end=" ")
  #  print()

# Q10. Prime Number Check

#num = int(input("Enter a number: "))

#if num <= 1:
 #   print("Not Prime")
#else:
 #   is_prime = True

  #  for i in range(2, num):
   #     if num % i == 0:
    #        is_prime = False
     #       break

#    if is_prime:
 #       print("Prime")
  #  else:
   #     print("Not Prime")

# Q11. Reverse a String Without Slicing

#text = input("Enter a string: ")

#for i in range(len(text) - 1, -1, -1):
 #   print(text[i], end=" ")

# Q12. Count Digits Using While Loop

#num = int(input("Enter a number: "))

#count = 0

#while num > 0:
 #   num = num // 10
  #  count += 1

# print("Digits =", count)

#Q13. Average Marks and Grade

#marks = 75

#if marks >= 90:
   # print("Grade A")

#elif marks > 70:
   # print("Grade B")

#elif marks > 50:
#    print("Grade C")

#else:
   # print("Fail")
 
#Q14. Continue and Break
#for i in range(1, 51):

 #   if i % 3 == 0:
  #      continue

   # if i % 7 == 0 and i > 30:
    #    break

    #print(i)

# Ques 15 factorial with while loop

#num = int(input("Enter a number: "))

#fact = 1
#i = num

#while i >= 1:
   # fact *= i
  #  i -= 1

#print("Factorial =", fact)

#Q16. Number Triangle Using Nested Loops

#for i in range(1, 6):

    #for j in range(1, i + 1):
        #print(j , end="")
#print()

# Ques 17 Perfect number check

#num = int(input("Enter a number: "))

#sum_of_factors = 0

#for i in range(1, num):
 #   if num % i == 0:
  #      sum_of_factors += i

#if sum_of_factors == num:
 #   print(num, "is a Perfect Number")
#else:
 #   print(num, "is NOT a Perfect Number")

#Ques18 Fibonacci Series Using While Loop

#n = int (input("Enter number of terms:"))

#a = 0
#b = 1
#count = 1

#while count <= n:
 #   print(a,end="")

  #  c = a + b
   ##b = c

    #count += 1

#Ques 19 Ticket price using nested if 
 
#age = int(input("Enter your age:"))
#student_id = input("Do you have a student ID (yes or no):")

#price = 0

#if age < 5:
 #   price = 0

#elif age <= 17:
    
 #   if student_id.lower() == "yes":
  #      price = 30
   # else:
    #    price = 50


#elif age <= 60:

# if student_id.lower()=="yes":
 #   price = 70
#else:
 #   price = 100 


#print("Ticket price $", price)

#Ques 20

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for num in range(start, end + 1):

    if num > 1:
        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
            count += 1

print("\nTotal Prime Numbers =", count)