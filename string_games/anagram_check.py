"""
Anagram Checker - A program to determine if two strings are anagrams

An anagram is a word or phrase formed by rearranging the letters of another,
such as "listen" and "silent".

Author: Your Name
Date: 2025
"""

from typing import Tuple

def are_anagrams(str1: str, str2: str) -> Tuple[bool, str]:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        str1 (str): First string to check
        str2 (str): Second string to check
    
    Returns:
        Tuple[bool, str]: A tuple containing:
            - bool: True if strings are anagrams, False otherwise
            - str: Explanation message
    
    Example:
        >>> are_anagrams("listen", "silent")
        (True, "The strings 'listen' and 'silent' are anagrams!")
    """
    # Convert to lowercase and remove spaces for better comparison
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    
    # Quick check: if lengths differ, they can't be anagrams
    if len(s1) != len(s2):
        return False, f"Length mismatch: '{str1}' ({len(s1)} chars) vs '{str2}' ({len(s2)} chars)"
    
    # Sort characters and compare
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    
    if sorted_s1 == sorted_s2:
        return True, f"The strings '{str1}' and '{str2}' are anagrams!"
    else:
        return False, f"The strings '{str1}' and '{str2}' are NOT anagrams."

def print_analysis(str1: str, str2: str) -> None:
    """
    Print detailed analysis of the anagram check.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
    """
    print("\n" + "="*50)
    print("ANAGRAM ANALYSIS")
    print("="*50)
    print(f"String 1: '{str1}'")
    print(f"String 2: '{str2}'")
    print("-"*50)
    
    # Show normalized strings
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    
    print(f"Normalized String 1: '{s1}'")
    print(f"Normalized String 2: '{s2}'")
    print(f"Sorted String 1: {sorted(s1)}")
    print(f"Sorted String 2: {sorted(s2)}")
    print("-"*50)

def main():
    """
    Main function to run the anagram checker program.
    """
    print("Welcome to the Anagram Checker!")
    print("This program checks if two strings are anagrams of each other.")
    
    # Get user input
    x = input("\nEnter the first string: ")
    y = input("Enter the second string: ")
    
    # Print analysis
    print_analysis(x, y)
    
    # Check if they are anagrams
    result, message = are_anagrams(x, y)
    print(f"\nResult: {message}")
    print("="*50)

def run_tests():
    """
    Run some test cases to demonstrate the function.
    """
    print("\n" + "="*50)
    print("RUNNING TEST CASES")
    print("="*50)
    
    test_cases = [
        ("listen", "silent"),
        ("race", "care"),
        ("hello", "world"),
        ("Dormitory", "Dirty room"),
        ("Astronomer", "Moon starer"),
        ("python", "typhon"),
        ("test", "tess")
    ]
    
    for str1, str2 in test_cases:
        result, message = are_anagrams(str1, str2)
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status} {message}")
    
    print("="*50)

if __name__ == "__main__":
    # Uncomment the next line to run tests instead of interactive mode
    run_tests()
    # main()






































