"""
What is a Tuple?
A tuple is an ordered, immutable (unchangeable) collection of elements in Python, 
typically defined using parentheses ().

Benefits of using Tuples over Lists:
1. Memory Efficiency: Tuples are more memory-efficient than lists (as demonstrated below).
2. Performance: Tuples are slightly faster to iterate over than lists.
3. Safety: Because they are immutable, data within a tuple is protected from accidental modification.
4. Dictionary Keys: Unlike lists, tuples can be used as keys in dictionaries because they are hashable.
"""
import sys


def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinate_tuple)} bytes") #56 bytes
    print(f"{sys.getsizeof(coordinate_list)} bytes") #72 bytes


main()