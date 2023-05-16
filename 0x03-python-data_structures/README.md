In this project, I am going to be doing tasks regarding Python data structures, with main focus on lists and tuples. The project aims to answer the following questions:

0. A function that prints all integers of a list
1. A function that retrieves an element at a given index from a list
2. A function that replaces an element at a given index in a list
3. A function prints all integers in a list in reverse
4. Write a function that replaces an element in a list at a specific position without modifying the original list 
5. Write a function that removes all characters c and C from a string.
6. Write a function that prints a matrix of integers.
7. Write a function that adds 2 tuples.
8. Write a function that returns a tuple with the length of a string and its first character.
9. Write a function that finds the biggest integer of a list.
10. Write a function that finds all multiples of 2 in a list.
11. Write a function that deletes the item at a specific position in a list.
12. Complete the source code in order to switch value of a and b
	#!/usr/bin/python3
a = 89
b = 10
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("a={:d} - b={:d}".format(a, b))

13. Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.

Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrome

14. Create a C function that prints some basic info about Python lists.

Prototype: void print_python_list_info(PyObject *p);
Format: see example
Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Start by reading:
listobject.h
object.h
Common Object Structures
List Objects
