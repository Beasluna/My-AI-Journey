"""
Project: Palindrome Checker Utility
Description: This script implements a function to identify palindromes 
(words that read the same backward as forward). 
Concepts: String slicing, Case normalization, and Boolean logic.
"""

def is_palindrome(word: str) -> bool:
    """
    Checks if a given string is a palindrome.
    
    Args:
        word (str): The word to verify.
        
    Returns:
        bool: True if it's a palindrome, False otherwise.
    """
    # Normalize the word to lowercase to ensure case-insensitive comparison
    clean_word = word.lower()

    # Reverse the string using Python's slicing technique [start:stop:step]
    # A step of -1 reads the string from right to left
    reversed_word = clean_word[::-1]

    # Return the comparison result
    return clean_word == reversed_word

# List of test cases including valid and invalid palindromes
test_words = ["reconocer", "Python", "AI", "radar", "Level", "Beatriz"]

if __name__ == "__main__":
    print(f"{'WORD':<15} | {'IS PALINDROME?'}")
    print("-" * 35)
    
    for w in test_words:
        result = is_palindrome(w)
        # Format the output for a clean, professional console view
        print(f"{w:<15} | {result}")
