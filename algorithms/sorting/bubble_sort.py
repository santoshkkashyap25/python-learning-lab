"""
Bubble Sort Algorithm - A simple sorting algorithm

Bubble Sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they're in the wrong order. The pass through the list
is repeated until the list is sorted.

Time Complexity: O(n²) worst and average case, O(n) best case (optimized)
Space Complexity: O(1)
"""

from typing import List, Tuple
import time

def bubble_sort(arr: List[int]) -> Tuple[List[int], int]:
    """
    Sort an array using bubble sort algorithm.
    
    Args:
        arr (List[int]): List of integers to sort
    
    Returns:
        Tuple[List[int], int]: A tuple containing:
            - List[int]: Sorted array
            - int: Number of comparisons made
    
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        ([11, 12, 22, 25, 34, 64, 90], 21)
    """
    n = len(arr)
    comparisons = 0
    
    # Create a copy to avoid modifying the original
    sorted_arr = arr.copy()
    
    for i in range(n):
        # Flag to detect if any swap happened in this pass
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            comparisons += 1
            
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap the elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return sorted_arr, comparisons

def optimized_bubble_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    """
    Optimized bubble sort with early termination and swap tracking.
    
    Args:
        arr (List[int]): List of integers to sort
    
    Returns:
        Tuple[List[int], int, int]: A tuple containing:
            - List[int]: Sorted array
            - int: Number of comparisons made
            - int: Number of swaps made
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    sorted_arr = arr.copy()
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            comparisons += 1
            
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return sorted_arr, comparisons, swaps

def print_sorting_process(arr: List[int]) -> None:
    """
    Visualize the bubble sort process step by step.
    
    Args:
        arr (List[int]): Array to sort and visualize
    """
    print("\n" + "="*60)
    print("BUBBLE SORT VISUALIZATION")
    print("="*60)
    print(f"Original array: {arr}")
    print("-"*60)
    
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(n):
        print(f"\nPass {i + 1}:")
        swapped = False
        
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                print(f"  Swap {sorted_arr[j]} and {sorted_arr[j + 1]}")
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
                print(f"  Array: {sorted_arr}")
        
        if not swapped:
            print("  No swaps needed - array is sorted!")
            break
    
    print(f"\nFinal sorted array: {sorted_arr}")
    print("="*60)

def run_performance_test():
    """
    Compare bubble sort performance with different array sizes.
    """
    print("\n" + "="*60)
    print("PERFORMANCE ANALYSIS")
    print("="*60)
    
    test_sizes = [10, 100, 500, 1000]
    
    for size in test_sizes:
        import random
        test_array = [random.randint(1, 1000) for _ in range(size)]
        
        start_time = time.time()
        _, comparisons = bubble_sort(test_array)
        end_time = time.time()
        
        print(f"Array size: {size:4d} | Comparisons: {comparisons:6d} | Time: {(end_time - start_time)*1000:.2f}ms")
    
    print("="*60)

def run_tests():
    """
    Run test cases to verify bubble sort implementation.
    """
    print("\n" + "="*60)
    print("BUBBLE SORT TEST CASES")
    print("="*60)
    
    test_cases = [
        ([5, 2, 9, 8, 2, 3, 99, 8, 7, 89, 7, 56, 0, 0, 8], "Mixed numbers"),
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([1], "Single element"),
        ([], "Empty array"),
        ([3, 3, 3, 3], "All same elements"),
        ([64, 34, 25, 12, 22, 11, 90], "Classic example")
    ]
    
    for i, (test_array, description) in enumerate(test_cases, 1):
        sorted_array, comparisons = bubble_sort(test_array)
        expected_sorted = sorted(test_array)
        
        status = "[PASS]" if sorted_array == expected_sorted else "[FAIL]"
        print(f"{status} Test {i}: {description}")
        print(f"  Input:    {test_array}")
        print(f"  Output:   {sorted_array}")
        print(f"  Expected: {expected_sorted}")
        print(f"  Comparisons: {comparisons}")
        print()
    
    print("="*60)

def main():
    """
    Main function to run the bubble sort demonstration.
    """
    print("Welcome to the Bubble Sort Algorithm!")
    print("This program demonstrates the bubble sort algorithm with visualizations and performance analysis.")
    
    # Example array from the original code
    example_array = [5, 2, 9, 8, 2, 3, 99, 8, 7, 89, 7, 56, 0, 0, 8]
    
    print(f"\nExample array: {example_array}")
    
    # Sort the array
    sorted_array, comparisons = bubble_sort(example_array)
    print(f"Sorted array: {sorted_array}")
    print(f"Number of comparisons: {comparisons}")
    
    # Run demonstrations
    print_sorting_process([5, 2, 9, 8, 2])
    run_tests()
    run_performance_test()

if __name__ == "__main__":
    main()
