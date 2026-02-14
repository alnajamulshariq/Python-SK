# str1 = 'this is a string'
# str2 = "this is also a string"
# str3 = """this is a string that can span multiple lines"""
# print(type(str3))


#concatenation
# str1 = 'Hello'
# str2 = 'World'
# str3 = str1 + ' ' + str2
# print(str3)


#length of a string
# str1 = 'Hello World'
# print(len(str1))


#indexing
# str1 = 'Hello World'
# print(str1[0]) # H
# print(str1[6]) # W


#slicing
# str1 = 'Hello World'
# print(str1[0:5]) # Hello
# print(str1[6:11]) # World
# str1 = 'Hello World'
# print(str1[:5]) # Hello
# str1 = 'Hello World'
# print(str1[6:]) # World
# str1 = 'Hello World'
# print(str1[:]) # Hello World
# str1 = 'Hello World'
# print(str1[::2]) # HloWrd
# str1 = 'Hello World'
# print(str1[1::2]) # el ol
# str1 = 'Hello World'
# print(str1[::-1]) # dlroW olleH
# str1 = 'Hello World'
# print(str1[::3]) # Hoo
# str1 = 'Hello World'
# print(str1[1::3]) # elW
# str1 = 'Hello World'
# print(str1[2::3]) # l r
# str1 = 'Hello World'
# print(str1[3::3]) # o l
# str1 = 'Hello World'
# print(str1[4::3]) #  W
# str1 = 'Hello World'
# print(str1[5::3]) # r
# str1 = 'Hello World'
# print(str1[6::3]) # l
# str1 = 'Hello World'
# print(str1[7::3]) # d
# str1 = 'Hello World'
# print(str1[8::3]) #
# str1 = 'Hello World'
# print(str1[9::3]) #
# str1 = 'Hello World'
# print(str1[10::3]) #
# str1 = 'Hello World'
# print(str1[11::3]) #
# str1 = 'Hello World'
# print(str1[12::3]) #


#slicing with negative step
# str1 = 'Hello World'
# print(str1[::-1]) # dlroW olleH
# str1 = 'Hello World'
# print(str1[::-2]) # drWolH
# str1 = 'Hello World'
# print(str1[::-3]) # lWl
# str1 = 'Hello World'
# print(str1[::-4]) # ool
# str1 = 'Hello World'
# print(str1[::-5]) # rH
# str1 = 'Hello World'
# print(str1[::-6]) # d
# str1 = 'Hello World'
# print(str1[::-7]) # l
# str1 = 'Hello World'
# print(str1[::-8]) # W
# str1 = 'Hello World'
# print(str1[::-9]) # o
# str1 = 'Hello World'
# print(str1[::-10]) # l
# str1 = 'Hello World'
# print(str1[::-11]) # H



# negative indexing and slicing
# str = "Apple"

# print(str[-3 : -1]) #pl
# str = "Apple"
# print(str[-3 : ]) #ple
# str = "Apple"
# print(str[ : -1]) #Appl
# str = "Apple"
# print(str[ : ]) #Apple
# str = "Apple"
# print(str[-1 : -3 : -1]) #el
# str = "Apple"
# print(str[-1 : -4 : -1]) #elP
# str = "Apple"
# print(str[-1 : -5 : -1]) #elPp
# str = "Apple"
# print(str[-1 : -6 : -1]) #elPpA
# str = "Apple"
# print(str[-2 : -4 : -1]) #pl
# str = "Apple"
# print(str[-2 : -5 : -1]) #plP
# str = "Apple"
# print(str[-2 : -6 : -1]) #plPpA
# str = "Apple"
# print(str[-3 : -5 : -1]) #Pp
# str = "Apple"
# print(str[-3 : -6 : -1]) #PpA
# str = "Apple"
# print(str[-4 : -6 : -1]) #pA




#strings functions
# str1 = 'Hello World'
# print(str1.endswith("rld")) # True
# print(str1.endswith("RLD")) # False

#string capitalization function capatalize string 1st character
# str1 = 'hello world'
# print(str1.capitalize()) # Hello world


#string replace function old value replace with new value
# str1 = 'Hello World'
# print(str1.replace('o', 'a')) # Hella Warld
# str1 = "I'm studying Python programming"
# print(str1.replace('Python', 'Java')) # I'm studying Java programming



#string find function find karta hai k kya yeh word humari string mein exist karta hai ya nahi
# str1 = 'Hello World'
# print(str1.find('World')) # 6
# str1 = 'Hello World'
# print(str1.find('world')) # -1



#string count function count karta hai k humari string mein koi word kitni baar exist karta hai
# str1 = 'Hello World'
# print(str1.count('o')) # 2
# str1 = 'Hello World'
# print(str1.count('O')) # 0


# strName = input("Enter your name: ")
# print("Your name length is: ", len(strName))




#Conditional statements

# light = "green"
# if (light == "green"):
#     print("You can go")
# elif (light == "yellow"):
#     print("You should slow down")
# elif (light == "red"):
#     print("You should stop")
# else:
#     print("Invalid traffic light color")


# marks = int(input("Enter your marks: "))
# if (marks >= 90 and marks <= 100):
#     print("You got A grade")
# elif (marks >= 80 and marks < 90):
#     print("You got B grade")
# elif (marks >= 70 and marks < 80):
#     print("You got C grade")
# elif (marks >= 60 and marks < 70):
#     print("You got D grade")
# else:
#     print("You got F grade")



#nested if statements
# age = int(input("Enter your age: "))
# if (age >= 18):
#     print("You are eligible to vote")
#     if (age >= 21):
#         print("You are eligible to drink")
#     else:
#         print("You are not eligible to drink")
# else:
#     print("You are not eligible to vote")


#check if a number is even or odd
# num = int(input("Enter a number: "))
# if (num % 2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")



#write a program to find the greatest of three numbers entered by the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if (num1 >= num2 and num1 >= num3):
#     print("The greatest number is: ", num1)
# elif (num2 >= num1 and num2 >= num3):
#     print("The greatest number is: ", num2)
# else:    
#     print("The greatest number is: ", num3)




#write a program to check if a number is a multiple of 7 or not
# num = int(input("Enter a number: "))
# if (num % 7 == 0):
#     print("The number is a multiple of 7")
# else:
#     print("The number is not a multiple of 7")