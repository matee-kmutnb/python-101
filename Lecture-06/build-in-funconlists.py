# Example list
numbers = [4, 2, 9, 1, 5, 6]

 # 1. len(): Get the length of the list
length = len(numbers)
print(f"Length of the list: {length}") # Output: Length of the list: 6

 # 2. sum(): Calculate the sum of all elements in the list
total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}") # Output: Sum of all elements:
27

 # 3. max(): Find the maximum value in the list
max_value = max(numbers)
print(f"Maximum value: {max_value}") # Output: Maximum value: 9

 # 4. min(): Find the minimum value in the list
min_value = min(numbers)
print(f"Minimum value: {min_value}") # Output: Minimum value: 1

 # 5. sorted(): Return a sorted version of the list
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}") # Output: Sorted list: [1, 2, 4,5, 6, 9]

 # 6. any(): Check if any element in the list is True
bool_list = [False, True, False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}") # Output: Is any element True?
True

 # 7. all(): Check if all elements in the list are True
all_true = all(bool_list)
print(f"Are all elements True? {all_true}") # Output: Are all elementsTrue? False

 # 8. list(): Convert an iterable to a list (if not already a list)
string = "hello"
char_list = list(string)
print(f"List of characters: {char_list}") # Output: List of characters: ['h', 'e', 'l', 'l', 'o']

 # 9. reversed(): Return a reverse iterator of the list
reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}") # Output: Reversed list: [6,5, 1, 9, 2, 4]

 # 10. enumerate(): Return an iterator of tuples containing index and value
enumerated_numbers = list(enumerate(numbers))
print(f"Enumerated list: {enumerated_numbers}")
 # Output: Enumerated list: [(0, 4), (1, 2), (2, 9), (3, 1), (4, 5), (5, 6)]