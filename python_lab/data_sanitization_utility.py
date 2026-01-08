"""
Project: Data Sanitization Utility
Description: This script defines a robust cleaning function that filters a list 
to ensure type integrity (integers only) and performs an ascending sort.
Concepts: Type validation, list filtering, and sorting.
"""

def clean_order(input_list:list):
    """
    Cleans the input list by removing non-integer elements and sorting the result.
    """
    print(f"Inspecting elements in the list: {input_list}")

    # Initialize a new list for integers
    int_list = []

    # Check for integers and skip other data types (strings, floats, lists, etc.)
    for element in input_list:
        if type(element) == int:
            int_list.append(element)
        else:
            # We log the skipped elements to maintain data transparency
            print(f"Skipping invalid element: {element} (Type: {type(element)})")

    # Sort the sanitized list from smallest to largest
    int_list.sort()
    
    return int_list

# Input dataset with mixed types (integers, strings, floats, and nested lists)
co_data = ["first", 12, 47, 0, -4, 23.02, [2, 3, 4, 8, -3], "last", 3, 100, -31]

# Execute the function and store the result
result = clean_order(co_data)

print("-" * 80)
print(f"Final cleaned and sorted list: {result}")
