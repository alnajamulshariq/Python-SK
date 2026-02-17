# marks = [90.6, 85.4, 78.9, 92.3, 88.5]
# print(marks)
# print(type(marks))
# print(marks[0])  # Accessing the first element

# student = ["Shariq", 20, "Computer Science", 3.8, "Karachi"]
# print(student)
# print(type(student))
# print(student[0])  # Accessing the first element

# student[0] = "Najam"
# print(student)  # Modifying the first element of the list


#slicing of list
# marks = [90.6, 85.4, 78.9, 92.3, 88.5]
# print(marks[1:4])  # Slicing from index 1 to 3
# print(marks[:3])   # Slicing from the beginning to index 2
# print(marks[2:])   # Slicing from index 2 to the end
# print(marks[-3:])  # Slicing the last three elements
# print(marks[-3:-1])  # Slicing from the third last to the second last element


#list methods

#append() method is used to add an element at the end of the list
# list = [2,1,3]
# list.append(4)
# print(list)

#sort() method is used to sort the elements of the list in ascending order

# list = [3, 1, 4, 2]
# list.sort()
# print(list)

# list = [3, 1, 4, 2]
# list.sort(reverse=True)  # Sort in descending order
# print(list)


#reverse() method is used to reverse the order of the elements in the list
# list = [1, 2, 3, 4, 5]
# list.reverse()
# print(list)


#insert() method is used to insert an element at a specific index in the list
# list = [2, 5, 1, 4, 3]
# list.insert(2, 10)  # Insert 10 at index 2
# print(list)


#remove() method is used to remove the first occurrence of a specified value from the list
# list = [1, 2, 3, 4, 5, 3, 3, 6]
# list.remove(3)  # Remove the first occurrence of 3
# print(list)


#pop() method is used to remove and return an element at a specific index (default is the last element)
# list = [1, 2, 3, 4, 5]
# list.pop(2)  # Remove and return the element at index 2
# print(list)  # Output: [1, 2, 4, 5]


#tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# tup = (1, 2, 3, 4, 5)
# print(tup)
# print(type(tup))
# print(tup[0])  # Accessing the first element of the tuple
# print(tup[1:4])  # Slicing the tuple from index 1 to 3



#tuple methods
#tuple index() method is used to find the index of the first occurrence of a specified value in the tuple
# tup = (1, 2, 3, 4, 5, 3)
# print(tup.index(3))  # Output: 2 (the index of the first occurrence of 3 on index 2)

#tuple count() method is used to count the number of occurrences of a specified value in the tuple
# tup = (1, 2, 3, 4, 5, 3)
# print(tup.count(3))  # Output: 2 (the number of occurrences of 3 in the tuple)



#write a program to ask the user to enter names of their 3 favorite movies and store them is a list.

# favorite_movies = []
# firstMovie = input("Enter the name of your first favorite movie: ")
# secondMovie = input("Enter the name of your second favorite movie: ")
# thirdMovie = input("Enter the name of your third favorite movie: ")
# favorite_movies.append(firstMovie)
# favorite_movies.append(secondMovie)
# favorite_movies.append(thirdMovie)
# print("Your favorite movies are:", favorite_movies)



#write a program to check if a list contains a palindrome of elements. (Hint: use copy() method).

# list1 = [1, 2, 3, 2, 1]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if list1 == copy_list1:
#     print("List 1 is a palindrome.")
# else:    
#     print("List 1 is not a palindrome.")



#write a program to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]
#store the above values in a list and sort them from "A" to "D".

# grades = ("C", "D", "A", "A", "B", "B", "A")
# print(grades.count("A"))  # Output: 3 (the number of occurrences of "A" in the tuple)

# grades = ["C", "D", "A", "A", "B", "B", "A"]
# grades.sort()  # Sort the list in ascending order (from "A" to "D")
# print(grades)  # Output: ['A', 'A', 'A', 'B', 'B', 'C', 'D']

