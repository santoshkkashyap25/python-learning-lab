"""
Binary Search Algorithm - Efficient searching in sorted arrays

Binary Search is a divide-and-conquer algorithm that searches for a target
value in a sorted array by repeatedly dividing the search interval in half.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

from typing import List, Tuple, Optional
import time

def binary_search(arr: List[int], target: int) -> Tuple[bool, int, int]:
    """
    Perform binary search on a sorted array.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    
    Returns:
        Tuple[bool, int, int]: A tuple containing:
            - bool: True if found, False otherwise
            - int: Index of the element (or -1 if not found)
            - int: Number of iterations/comparisons
    
    Example:
        >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
        (True, 4, 3)
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        print(f"Iteration {iterations}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            return True, mid, iterations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False, -1, iterations

def binary_search_verbose(arr: List[int], target: int) -> None:
    """
    Perform binary search with detailed step-by-step output.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    """
    print("\n" + "="*70)
    print("BINARY SEARCH - STEP BY STEP")
    print("="*70)
    print(f"Searching for {target} in array: {arr}")
    print("-"*70)
    
    left, right = 0, len(arr) - 1
    iteration = 0
    
    while left <= right:
        iteration += 1
        mid = (left + right) // 2
        
        print(f"\nIteration {iteration}:")
        print(f"  Search range: indices [{left}, {right}]")
        print(f"  Middle index: {mid}")
        print(f"  Middle value: {arr[mid]}")
        print(f"  Comparing {target} with {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  ✓ Found {target} at index {mid}!")
            print(f"  Total iterations: {iteration}")
            print("="*70)
            return
        elif arr[mid] < target:
            print(f"  {target} > {arr[mid]}, search right half")
            left = mid + 1
        else:
            print(f"  {target} < {arr[mid]}, search left half")
            right = mid - 1
    
    print(f"\n✗ {target} not found in the array")
    print(f"Total iterations: {iteration}")
    print("="*70)

def compare_with_linear_search(arr: List[int], target: int) -> None:
    """
    Compare binary search performance with linear search.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    """
    print("\n" + "="*70)
    print("BINARY SEARCH vs LINEAR SEARCH COMPARISON")
    print("="*70)
    print(f"Array size: {len(arr)}")
    print(f"Searching for: {target}")
    print("-"*70)
    
    # Binary Search
    start_time = time.time()
    found, index, binary_iterations = binary_search(arr, target)
    binary_time = time.time() - start_time
    
    # Linear Search
    start_time = time.time()
    linear_iterations = 0
    linear_found = False
    linear_index = -1
    
    for i, val in enumerate(arr):
        linear_iterations += 1
        if val == target:
            linear_found = True
            linear_index = i
            break
    
    linear_time = time.time() - start_time
    
    print(f"Binary Search:")
    print(f"  Found: {found} at index {index}")
    print(f"  Iterations: {binary_iterations}")
    print(f"  Time: {binary_time*1000:.6f} ms")
    
    print(f"\nLinear Search:")
    print(f"  Found: {linear_found} at index {linear_index}")
    print(f"  Iterations: {linear_iterations}")
    print(f"  Time: {linear_time*1000:.6f} ms")
    
    print(f"\nEfficiency Ratio (Linear/Binary): {linear_iterations/binary_iterations:.2f}x")
    print("="*70)

def run_comprehensive_tests():
    """
    Run various test cases to demonstrate binary search.
    """
    print("\n" + "="*70)
    print("BINARY SEARCH TEST SUITE")
    print("="*70)
    
    # Test cases: (array, target, expected_result)
    test_cases = [
        (list(range(1, 10000)), 43, True),  # Original test case
        (list(range(1, 101)), 1, True),     # First element
        (list(range(1, 101)), 100, True),   # Last element
        (list(range(1, 101)), 50, True),    # Middle element
        (list(range(1, 101)), 0, False),    # Not found (too small)
        (list(range(1, 101)), 101, False),  # Not found (too large)
        ([], 5, False),                     # Empty array
        ([5], 5, True),                     # Single element - found
        ([5], 3, False),                    # Single element - not found
        (list(range(2, 100, 2)), 50, True), # Even numbers
        (list(range(1, 1000, 3)), 100, False) # Step of 3, target not in sequence
    ]
    
    for i, (arr, target, expected) in enumerate(test_cases, 1):
        found, index, iterations = binary_search(arr, target)
        
        status = "[PASS]" if found == expected else "[FAIL]"
        print(f"{status} Test {i}: Search for {target}")
        print(f"  Array size: {len(arr):4d} | Result: {found:5} | Index: {index:3d} | Iterations: {iterations:2d}")
    
    print("="*70)

def demonstrate_search_complexity():
    """
    Demonstrate how binary search complexity grows logarithmically.
    """
    print("\n" + "="*70)
    print("BINARY SEARCH COMPLEXITY DEMONSTRATION")
    print("="*70)
    print("Array Size | Max Iterations (log₂n) | Actual Iterations")
    print("-"*70)
    
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    
    for size in sizes:
        arr = list(range(1, size + 1))
        target = size // 2  # Search for middle element (worst case for binary search)
        
        _, _, iterations = binary_search(arr, target)
        max_iterations = len(bin(size)) - 1  # log₂n
        
        print(f"{size:10d} | {max_iterations:22d} | {iterations:17d}")
    
    print("="*70)

def main():
    """
    Main function to run binary search demonstrations.
    """
    print("Welcome to the Binary Search Algorithm!")
    print("This program demonstrates binary search with detailed analysis and comparisons.")
    
    # Original test case from the code
    original_array = list(range(1, 10000))
    target = 43
    
    print(f"\nOriginal Test Case:")
    print(f"Array: 1 to 9999")
    print(f"Target: {target}")
    
    binary_search_verbose(original_array, target)
    
    # Additional demonstrations
    compare_with_linear_search(list(range(1, 1001)), 500)
    run_comprehensive_tests()
    demonstrate_search_complexity()

if __name__ == "__main__":
    main()
