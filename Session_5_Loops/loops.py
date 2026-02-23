#while loop kaise kaam karta hai while loop ka matlab hai jab tak condition true hai tab tak loop chalega
# count = 1
# while count <= 5:
#     print("Shariq Najam")
#     count += 1


# i = 1
# while i <= 10:
#     print("Shariq", i)
#     i += 1


#print number from 1 to 10 using while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


#print number from 5 to 1 using while loop
# i = 5
# while i >=1:
#     print(i)
#     i -= 1



#print numbers from 1 to 100 using while loop
# i = 1
# while i <=100:
#     print(i)
#     i += 1



#print number from 100 to 1 using while loop
# i = 100
# while i >=1:
#     print(i)
#     i -= 1



#print the multiplication table of a number n
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n*i)
#     i += 1


#print the element of the following list using while loop
#[1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1



#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found at index", i)
#     else:
#         print("Finding.....", i)    
#     i += 1



#break and continue statement in while loop

#break use hota hai loop ko rokne ke liye jab hume kisi condition par loop ko stop karna hota hai
#continue use hota hai loop ke current iteration ko skip karne ke liye jab hume kisi condition par loop ke current iteration ko skip karna hota hai

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found at index", i)
#         break
#     else:
#         print("Finding.....", i)    
#     i += 1


# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1


#print even numbers 
# i = 0
# while i <= 10:
#     if i % 2 != 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

#print odd numbers
# i = 0
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1





#For loop in Python
#for loop ka matlab hai ki hum kisi sequence ke elements par ek ek karke loop chalate hain for loop ka syntax hai for variable in sequence: body of the loop

# list = [1,2,3,4,5]
# for num in list:
#     print(num)


# veggies = ["tomato", "potato", "onion", "carrot"]
# for veg in veggies:
#     print(veg)


# str = "ShariqNajam"

# for char in str:
#     print(char)



#lets practice
#using for
#print the element of the following list using for loop:
#[1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# for num in nums:
#     print(num)


#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

# tup = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# idx = 0
# for num in tup:
#     if num == x:
#         print("Found at index", idx)
#         break
#     idx += 1



#range function in for loop
#range function ka matlab hai ki hum ek sequence of numbers generate kar sakte hain range function ka syntax hai range(start, stop, step) start se lekar stop tak step ke interval par numbers generate karta hai
# seq = range(10)
# for i in seq:
#     print(i)

# for i in range(5): #range (stop)
#     print(i)


# for i in range(2, 11): #range (start, stop)
#     print(i)

# for i in range(2, 11, 2): #range (start, stop, step)
#     print(i)

#print even numbers from range strat, stop, step
# for i in range(2, 101, 2):
#     print(i)


#print odd numbers from range start, stop, step
# for i in range(1, 101, 2):
#     print(i)


#lets practice:
#using for & range()
#print numbers from 1 to 100.

# for i in range(1, 101):
#     print(i)



#print numbers from 100 to 1

# for i in range(100, 0, -1):
#     print(i)


#print the multiplication table of a number n
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)



#Pass statement in Python
#pass statement ka matlab hai ki hum kisi block of code ko empty chhod sakte hain pass statement ka syntax hai pass
# for i in range(5):
#     pass              #ye block of code ko empty chhod deta hai



#Let's practice:
#write a program to find the sum of first natural numbers. (using while)

# num = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= num:
#     sum += i
#     i += 1
# print("The sum of first", num, "natural numbers is:", sum)




#write a program to find the factorial of first natural numbers. (using for)
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial *= i
# print("The factorial of", num, "is:", factorial)



