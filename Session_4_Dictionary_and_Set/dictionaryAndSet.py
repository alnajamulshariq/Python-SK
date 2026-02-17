# stdInfo = {
#     "name": "Shariq Najam",
#     "subjects": ["Math", "Physics", "Chemistry"],
#     "topics": ("OOP", "Data Structures", "Algorithms"),
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# print(stdInfo)
# print(type(stdInfo))


# stdInfo = {
#     "name": "Shariq Najam",
#     "marks": {
#         "Math": 85,
#         "Physics": 90,
#         "Chemistry": 80,
#     },
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# print(stdInfo)
# print(type(stdInfo))
# print(stdInfo["marks"])
# print(stdInfo["marks"]["Math"])


#Dictionary Methods
#.keys()
# stdInfo = {
#     "name": "Shariq Najam",
#     "marks": {
#         "Math": 85,
#         "Physics": 90,
#         "Chemistry": 80,
#     },
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# print(stdInfo.keys())


# #type casting to list
# print(list(stdInfo.keys()))
# #length of dictionary
# print(len(list(stdInfo.keys())))


#values() method in dictionary
# stdInfo = {
#     "name": "Shariq Najam",
#     "marks": {
#         "Math": 85,
#         "Physics": 90,
#         "Chemistry": 80,
#     },
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# print(stdInfo.values())
# #type casting to list
# print(list(stdInfo.values()))



#items() method in dictionary
#item method returns a list of tuples where each tuple contains a key-value pair from the dictionary
# stdInfo = {
#     "name": "Shariq Najam",
#     "marks": {
#         "Math": 85,
#         "Physics": 90,
#         "Chemistry": 80,
#     },
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# print(stdInfo.items())
# #type casting to list
# print(list(stdInfo.items()))



#get() method in dictionary
#get method is used to access the value of a key in a dictionary. It takes the key as an argument and returns the corresponding value. If the key is not found, it returns None or a default value if provided.

# stdInfo = {
#     "name": "Shariq Najam",
#     "marks": {
#         "Math": 85,
#         "Physics": 90,
#         "Chemistry": 80,
#     },
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# print(stdInfo.get("name"))  # Output: Shariq Najam
# print(stdInfo.get("age"))   # Output: 22
# print(stdInfo.get("gender"))  # Output: None (key not found)
# print(stdInfo.get("gender", "Not Specified"))  # Output: Not Specified (key not found, default value returned)




#update() method in dictionary
#update method is used to update the values of existing keys or add new key-value pairs to a dictionary. It takes another dictionary as an argument and updates the original dictionary with the key-value pairs from the provided dictionary.
# stdInfo = {
#     "name": "Shariq Najam",
#     "marks": {
#         "Math": 85,
#         "Physics": 90,
#         "Chemistry": 80,
#     },
#     "age": 22,
#     "height": 5.8,
#     "isAdult": True,
#     "city": "Karachi",
#     "country": "Pakistan",
# }

# # Update existing key
# stdInfo.update({"age": 23})
# print(stdInfo["age"])  # Output: 23





#Sets in Python
# A set is an unordered collection of unique elements. It is defined using curly braces {} or
# the set() constructor. Sets are mutable, meaning you can add or remove elements from them. However, since sets are unordered, they do not support indexing or slicing.

# collection = {1, 2, 2, 2, 3, 3, 3, 3, 4, 5, "Hello", "Hello", "World", "World"}
# print(collection)
# print(type(collection))
# print(len(collection))  # Output: 7 (unique elements only)

# #kaise empty set banayein?
# # empty_set = {}  # This creates an empty dictionary, not a set
# empty_set = set()  # This creates an empty set
# print(empty_set)
# print(type(empty_set))


#Methods in Set
#add() method in set
# The add() method is used to add an element to a set. If the element already exists in the set, it will not be added again since sets only contain unique elements.


# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)  # Duplicate element, will not be added

# print(collection)  # Output: {1, 2}



# #remove() method in set
# # The remove() method is used to remove a specific element from a set. If the element is not found in the set, it raises a KeyError.
# collection = {1, 2, 3, 4, 5}
# collection.remove(3)  # Removes the element 3 from the set



# clear() method in set
# The clear() method is used to remove all elements from a set, resulting in an empty set.
# collection = {1, 2, 3, 4, 5}
# collection.clear()  # Removes all elements from the set
# print(collection)  # Output: set() (empty set)



#pop() method in set
# The pop() method is used to remove and return an arbitrary element from a set. Since sets are unordered, there is no guarantee which element will be removed. If the set is empty, it raises a KeyError.
# collection = {1, 2, 3, 4, 5}
# removed_element = collection.pop()  # Removes and returns an arbitrary element
# print(removed_element)  # Output: (arbitrary element from the set)
# print(collection)  # Output: (remaining elements in the set)


# collection = {"Muhammad ","Shariq", "Najam", "Ansari"}
# print(collection.pop())  # Output: (arbitrary element from the set)
# print(collection)  # Output: (remaining elements in the set)



#union method in set
# The union() method is used to combine two sets and return a new set that contains all the unique elements from both sets.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}




#intersection method in set
# The intersection() method is used to find the common elements between two sets and return a new set that contains only those common elements.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1.intersection(set2))  # Output: {3}




# store following words meanings in a python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

# dictionary = {
#     "cat": "a small animal",
#     "table": ["a piece of furniture", "list of facts & figures"]
# }

# print(dictionary)



# you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "Pyhton", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"


# subjects = {"Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"}
# print(subjects)  # Output: {'Pyhton', 'Java', 'C++', 'Python', 'JavaScript', 'C'}
# print(len(subjects))  # Output: 6 (unique subjects only are counted)




#write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject names as key & marks as value.


# marks = {}
# marks["Math"] = int(input("Enter marks for Math: "))
# marks["Physics"] = int(input("Enter marks for Physics: "))
# marks["Chemistry"] = int(input("Enter marks for Chemistry: "))

# print(marks)




# figure out a way to store 9 & 9.0 as separate values in a set. (You can take help of built-in data types in python)

# values = {9, 9.0}
# print(values)  # Output: {9}
# In Python, the integer 9 and the floating-point number 9.0 are considered equal when it comes to sets, as they have the same value. Therefore, only one of them will be stored in the set, resulting in {9}.

# values = {9, "9.0"}
# print(values)  # Output: {9, '9.0'}


values = {
    "float": 9.0,
    "int": 9,
}

print(values)  # Output: {'float': 9.0, 'int': 9}