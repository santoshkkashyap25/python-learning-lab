"""
Linear Search Algorithm - Simple sequential searching

Linear Search sequentially checks each element of the list until a match
is found or the whole list has been searched.

Time Complexity: O(n) - worst, average, and best case
Space Complexity: O(1)
"""

from typing import List, Tuple, Optional
import time
import random

def linear_search(arr: List[int], target: int) -> Tuple[bool, int, int]:
    """
    Perform linear search on an array.
    
    Args:
        arr (List[int]): Array to search in
        target (int): Value to search for
    
    Returns:
        Tuple[bool, int, int]: A tuple containing:
            - bool: True if found, False otherwise
            - int: Index of the element (or -1 if not found)
            - int: Number of comparisons made
    
    Example:
        >>> linear_search([4, 2, 7, 1, 3], 7)
        (True, 2, 3)
    """
    for i, value in enumerate(arr):
        if value == target:
            return True, i, i + 1  # i+1 because we start counting from 1
    return False, -1, len(arr)

def linear_search_verbose(arr: List[int], target: int) -> None:
    """
    Perform linear search with detailed step-by-step output.
    
    Args:
        arr (List[int]): Array to search in
        target (int): Value to search for
    """
    print("\n" + "="*60)
    print("LINEAR SEARCH - STEP BY STEP")
    print("="*60)
    print(f"Searching for {target} in array: {arr}")
    print("-"*60)
    
    for i, value in enumerate(arr):
        print(f"Step {i + 1}: Checking index {i} (value: {value})")
        
        if value == target:
            print(f"  ✓ Found {target} at index {i}!")
            print(f"  Total comparisons: {i + 1}")
            print("="*60)
            return
        else:
            print(f"  {value} ≠ {target}, continue searching...")
    
    print(f"\n✗ {target} not found in the array")
    print(f"Total comparisons: {len(arr)}")
    print("="*60)

def find_all_occurrences(arr: List[int], target: int) -> List[int]:
    """
    Find all occurrences of a target value in an array.
    
    Args:
        arr (List[int]): Array to search in
        target (int): Value to search for
    
    Returns:
        List[int]: List of indices where the target was found
    """
    occurrences = []
    for i, value in enumerate(arr):
        if value == target:
            occurrences.append(i)
    return occurrences

def compare_search_performance():
    """
    Compare linear search performance with different array sizes and target positions.
    """
    print("\n" + "="*70)
    print("LINEAR SEARCH PERFORMANCE ANALYSIS")
    print("="*70)
    
    test_sizes = [100, 1000, 5000, 10000]
    
    for size in test_sizes:
        arr = list(range(1, size + 1))
        
        # Test different target positions
        test_cases = [
            (1, "First element"),
            (size // 2, "Middle element"),
            (size, "Last element"),
            (size + 1, "Not found")
        ]
        
        print(f"\nArray size: {size}")
        print("-" * 50)
        
        for target, description in test_cases:
            start_time = time.time()
            found, index, comparisons = linear_search(arr, target)
            search_time = time.time() - start_time
            
            print(f"  {description:15} | Found: {found:5} | Index: {index:5d} | Comparisons: {comparisons:6d} | Time: {search_time*1000:.4f}ms")
    
    print("="*70)

def demonstrate_best_worst_case():
    """
    Demonstrate best case, worst case, and average case scenarios.
    """
    print("\n" + "="*60)
    print("BEST, WORST, AND AVERAGE CASE SCENARIOS")
    print("="*60)
    
    arr = list(range(1, 21))  # Array of 20 elements
    print(f"Test array: {arr}")
    print("-"*60)
    
    # Best case: target is first element
    print("\n1. BEST CASE - Target is first element")
    found, index, comparisons = linear_search(arr, 1)
    print(f"   Searching for 1: Found at index {index}, {comparisons} comparison(s)")
    
    # Worst case: target is last element
    print("\n2. WORST CASE - Target is last element")
    found, index, comparisons = linear_search(arr, 20)
    print(f"   Searching for 20: Found at index {index}, {comparisons} comparison(s)")
    
    # Worst case: target not found
    print("\n3. WORST CASE - Target not found")
    found, index, comparisons = linear_search(arr, 25)
    print(f"   Searching for 25: Not found, {comparisons} comparison(s)")
    
    # Average case: target is in the middle
    print("\n4. AVERAGE CASE - Target is in middle")
    found, index, comparisons = linear_search(arr, 10)
    print(f"   Searching for 10: Found at index {index}, {comparisons} comparison(s)")
    
    print("="*60)

def run_comprehensive_tests():
    """
    Run various test cases to verify linear search implementation.
    """
    print("\n" + "="*60)
    print("LINEAR SEARCH TEST SUITE")
    print("="*60)
    
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, True, "Middle element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, True, "First element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, True, "Last element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, False, "Not found"),
        ([], 5, False, "Empty array"),
        ([5], 5, True, "Single element - found"),
        ([5], 3, False, "Single element - not found"),
        ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 12, True, "Even numbers"),
        ([1, 1, 1, 1, 1], 1, True, "All same elements"),
        ([-5, -3, -1, 0, 1, 3, 5], -1, True, "Negative numbers")
    ]
    
    for i, (arr, target, expected, description) in enumerate(test_cases, 1):
        found, index, comparisons = linear_search(arr, target)
        
        status = "[PASS]" if found == expected else "[FAIL]"
        print(f"{status} Test {i}: {description}")
        print(f"  Array: {arr}")
        print(f"  Target: {target}")
        print(f"  Result: Found={found} at index={index}, Comparisons={comparisons}")
        print()
    
    print("="*60)

def demonstrate_multiple_occurrences():
    """
    Demonstrate finding all occurrences of a value.
    """
    print("\n" + "="*60)
    print("FINDING MULTIPLE OCCURRENCES")
    print("="*60)
    
    test_array = [1, 5, 2, 5, 3, 5, 4, 5, 5]
    target = 5
    
    print(f"Array: {test_array}")
    print(f"Searching for all occurrences of: {target}")
    print("-"*60)
    
    occurrences = find_all_occurrences(test_array, target)
    
    if occurrences:
        print(f"Found {target} at indices: {occurrences}")
        print(f"Total occurrences: {len(occurrences)}")
    else:
        print(f"No occurrences of {target} found")
    
    print("="*60)

def main():
    """
    Main function to run linear search demonstrations.
    """
    print("Welcome to the Linear Search Algorithm!")
    print("This program demonstrates linear search with detailed analysis and comparisons.")
    
    # Original test case from the code
    print(f"\nOriginal Test Case:")
    linear_search_verbose(list(range(1, 10)), 4)
    
    # Additional demonstrations
    demonstrate_best_worst_case()
    demonstrate_multiple_occurrences()
    run_comprehensive_tests()
    compare_search_performance()

if __name__ == "__main__":
    main()
