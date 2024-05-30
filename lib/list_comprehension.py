#!/usr/bin/env python3
# This line specifies that this script should be executed using the Python 3 interpreter.

# This function takes a list of integers as input and returns a new list containing only the even elements.
def return_evens(num_list):
    # The list comprehension [x for x in num_list if x % 2 == 0] creates a new list
    # where each element x is included if it is even (x % 2 == 0).
    return [x for x in num_list if x % 2 == 0]

# This function takes a list of sentence strings as input and returns a new list
# where each sentence has an exclamation mark added to the end.
def make_exclamation(sentence_list):
    # The list comprehension [sentence + "!" for sentence in sentence_list] creates a new list
    # where each sentence string has an exclamation mark concatenated to the end.
    return [sentence + "!" for sentence in sentence_list]
