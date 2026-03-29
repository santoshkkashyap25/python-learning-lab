"""
Recursive Binary Search Algorithm - Divide and conquer approach

Recursive Binary Search implements the same logic as iterative binary search
but uses recursion instead of a loop to divide the search space.

Time Complexity: O(log n)
Space Complexity: O(log n) due to recursion call stack
"""

from typing import List, Tuple
import time

def binary_search_recursive(arr: List[int], target: int, left: int, right: int, depth: int = 0) -> Tuple[int, int]:
    """
    Perform recursive binary search on a sorted array.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
        left (int): Left boundary of search space
        right (int): Right boundary of search space
        depth (int): Current recursion depth (for tracking)
    
    Returns:
        Tuple[int, int]: A tuple containing:
            - int: Index of the element (or -1 if not found)
            - int: Number of recursive calls made
    
    Example:
        >>> binary_search_recursive([1, 2, 3, 4, 5], 3, 0, 4)
        (2, 2)
    """
    # Base case: if left > right, element is not present
    if left > right:
        return -1, depth + 1
    
    # Calculate middle index
    mid = (left + right) // 2
    
    print(f"  Recursion depth {depth}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
    
    # Check if middle element is the target
    if arr[mid] == target:
        return mid, depth + 1
    # If target is smaller, search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1, depth + 1)
    # If target is larger, search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right, depth + 1)

def binary_search_recursive_wrapper(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Wrapper function for recursive binary search.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    
    Returns:
        Tuple[int, int]: A tuple containing:
            - int: Index of the element (or -1 if not found)
            - int: Number of recursive calls made
    """
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

def binary_search_recursive_verbose(arr: List[int], target: int) -> None:
    """
    Perform recursive binary search with detailed step-by-step output.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    """
    print("\n" + "="*70)
    print("RECURSIVE BINARY SEARCH - STEP BY STEP")
    print("="*70)
    print(f"Searching for {target} in array: {arr}")
    print("-"*70)
    
    index, calls = binary_search_recursive_wrapper(arr, target)
    
    if index != -1:
        print(f"\n✓ Found {target} at index {index}!")
    else:
        print(f"\n✗ {target} not found in the array")
    
    print(f"Total recursive calls: {calls}")
    print("="*70)

def compare_recursive_iterative():
    """
    Compare recursive and iterative binary search approaches.
    """
    print("\n" + "="*70)
    print("RECURSIVE vs ITERATIVE BINARY SEARCH COMPARISON")
    print("="*70)
    
    # Create test array
    arr = list(range(1, 1001))
    test_targets = [1, 250, 500, 750, 1000, 1001]  # Mix of found and not found
    
    print(f"Array size: {len(arr)}")
    print("-"*70)
    
    for target in test_targets:
        # Recursive approach
        start_time = time.time()
        recursive_index, recursive_calls = binary_search_recursive_wrapper(arr, target)
        recursive_time = time.time() - start_time
        
        # Iterative approach
        start_time = time.time()
        iterative_index, iterative_iterations = binary_search_iterative(arr, target)
        iterative_time = time.time() - start_time
        
        print(f"Target {target:4d}:")
        print(f"  Recursive: Index={recursive_index:4d}, Calls={recursive_calls:2d}, Time={recursive_time*1000:.4f}ms")
        print(f"  Iterative: Index={iterative_index:4d}, Steps={iterative_iterations:2d}, Time={iterative_time*1000:.4f}ms")
    
    print("="*70)

def binary_search_iterative(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Iterative binary search for comparison purposes.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    
    Returns:
        Tuple[int, int]: A tuple containing:
            - int: Index of the element (or -1 if not found)
            - int: Number of iterations made
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid, iterations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, iterations

def visualize_recursion_tree(arr: List[int], target: int) -> None:
    """
    Visualize the recursion tree for binary search.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Value to search for
    """
    print("\n" + "="*70)
    print("RECURSION TREE VISUALIZATION")
    print("="*70)
    print(f"Searching for {target} in array: {arr}")
    print("-"*70)
    
    def search_with_visualization(arr: List[int], target: int, left: int, right: int, depth: int = 0) -> int:
        if left > right:
            print(f"  {'  ' * depth}└── Base case: left ({left}) > right ({right}) - not found")
            return -1
        
        mid = (left + right) // 2
        
        print(f"  {'  ' * depth}├── Range [{left}:{right}], mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"  {'  ' * depth}└── Found {target} at index {mid}!")
            return mid
        elif arr[mid] > target:
            print(f"  {'  ' * depth}└── {target} < {arr[mid]}, search left half")
            return search_with_visualization(arr, target, left, mid - 1, depth + 1)
        else:
            print(f"  {'  ' * depth}└── {target} > {arr[mid]}, search right half")
            return search_with_visualization(arr, target, mid + 1, right, depth + 1)
    
    result = search_with_visualization(arr, target, 0, len(arr) - 1)
    print("="*70)

def run_comprehensive_tests():
    """
    Run various test cases to verify recursive binary search implementation.
    """
    print("\n" + "="*70)
    print("RECURSIVE BINARY SEARCH TEST SUITE")
    print("="*70)
    
    test_cases = [
        (list(range(1, 100)), 50, True, "Middle element"),
        (list(range(1, 100)), 1, True, "First element"),
        (list(range(1, 100)), 99, True, "Last element"),
        (list(range(1, 100)), 0, False, "Not found (too small)"),
        (list(range(1, 100)), 100, False, "Not found (too large)"),
        ([], 5, False, "Empty array"),
        ([5], 5, True, "Single element - found"),
        ([5], 3, False, "Single element - not found"),
        (list(range(2, 200, 2)), 100, True, "Even numbers"),
        (list(range(1, 50, 3)), 25, False, "Step of 3, target not in sequence")
    ]
    
    for i, (arr, target, expected, description) in enumerate(test_cases, 1):
        index, calls = binary_search_recursive_wrapper(arr, target)
        found = index != -1
        
        status = "[PASS]" if found == expected else "[FAIL]"
        print(f"{status} Test {i}: {description}")
        print(f"  Array size: {len(arr):3d} | Target: {target:3d} | Index: {index:3d} | Calls: {calls:2d}")
    
    print("="*70)

def analyze_recursion_depth():
    """
    Analyze recursion depth for different array sizes.
    """
    print("\n" + "="*70)
    print("RECURSION DEPTH ANALYSIS")
    print("="*70)
    print("Array Size | Max Depth (log₂n) | Actual Depth")
    print("-"*70)
    
    sizes = [8, 16, 32, 64, 128, 256, 512, 1024]
    
    for size in sizes:
        arr = list(range(1, size + 1))
        target = size // 2  # Middle element
        
        _, depth = binary_search_recursive_wrapper(arr, target)
        max_depth = len(bin(size)) - 1  # log₂n
        
        print(f"{size:10d} | {max_depth:16d} | {depth:12d}")
    
    print("="*70)

def main():
    """
    Main function to run recursive binary search demonstrations.
    """
    print("Welcome to the Recursive Binary Search Algorithm!")
    print("This program demonstrates recursive binary search with detailed analysis.")
    
    # Original test case from the code
    original_array = [20, 34, 56, 67, 89, 100, 678]
    target = 67
    
    print(f"\nOriginal Test Case:")
    print(f"Array: {original_array}")
    print(f"Target: {target}")
    
    binary_search_recursive_verbose(original_array, target)
    
    # Additional demonstrations
    visualize_recursion_tree(original_array, target)
    compare_recursive_iterative()
    run_comprehensive_tests()
    analyze_recursion_depth()

if __name__ == "__main__":
    main()
