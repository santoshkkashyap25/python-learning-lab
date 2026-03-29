"""
Factorial Calculation - Iterative and Recursive Approaches

Factorial of a non-negative integer n, denoted by n!, is the product of all
positive integers less than or equal to n. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.

Mathematical definition:
- n! = 1 for n = 0
- n! = n × (n-1) × (n-2) × ... × 1 for n > 0

Time Complexity: O(n) for both iterative and recursive
Space Complexity: O(1) for iterative, O(n) for recursive (call stack)
"""

from typing import List, Tuple
import time

def factorial_iterative(n: int) -> Tuple[int, int]:
    """
    Calculate factorial using iterative approach.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        Tuple[int, int]: A tuple containing:
            - int: Factorial of n
            - int: Number of multiplications performed
    
    Raises:
        ValueError: If n is negative
    
    Example:
        >>> factorial_iterative(5)
        (120, 5)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0:
        return 1, 0
    
    result = 1
    multiplications = 0
    
    for i in range(1, n + 1):
        result *= i
        multiplications += 1
    
    return result, multiplications

def factorial_recursive(n: int, depth: int = 0) -> Tuple[int, int]:
    """
    Calculate factorial using recursive approach.
    
    Args:
        n (int): Non-negative integer
        depth (int): Current recursion depth (for tracking)
    
    Returns:
        Tuple[int, int]: A tuple containing:
            - int: Factorial of n
            - int: Number of recursive calls made
    
    Raises:
        ValueError: If n is negative
    
    Example:
        >>> factorial_recursive(5)
        (120, 6)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0:
        return 1, depth + 1
    
    # Recursive case: n! = n × (n-1)!
    sub_result, calls = factorial_recursive(n - 1, depth + 1)
    return n * sub_result, calls

def factorial_recursive_verbose(n: int) -> None:
    """
    Calculate factorial with detailed recursive process visualization.
    
    Args:
        n (int): Non-negative integer
    """
    print("\n" + "="*60)
    print("FACTORIAL - RECURSIVE PROCESS VISUALIZATION")
    print("="*60)
    print(f"Calculating {n}!")
    print("-"*60)
    
    def recursive_helper(n: int, depth: int = 0) -> int:
        indent = "  " * depth
        
        if n == 0:
            print(f"{indent}factorial(0) = 1 (base case)")
            return 1
        
        print(f"{indent}factorial({n}) = {n} × factorial({n-1})")
        sub_result = recursive_helper(n - 1, depth + 1)
        result = n * sub_result
        print(f"{indent}factorial({n}) = {n} × {sub_result} = {result}")
        
        return result
    
    result = recursive_helper(n)
    print(f"\nFinal result: {n}! = {result}")
    print("="*60)

def compare_iterative_recursive():
    """
    Compare iterative and recursive factorial approaches.
    """
    print("\n" + "="*70)
    print("ITERATIVE vs RECURSIVE FACTORIAL COMPARISON")
    print("="*70)
    
    test_values = [5, 10, 15, 20]
    
    for n in test_values:
        print(f"\nCalculating {n}!:")
        print("-" * 40)
        
        # Iterative approach
        start_time = time.time()
        iter_result, iter_ops = factorial_iterative(n)
        iter_time = time.time() - start_time
        
        # Recursive approach
        start_time = time.time()
        rec_result, rec_calls = factorial_recursive(n)
        rec_time = time.time() - start_time
        
        print(f"Iterative: Result={iter_result}, Operations={iter_ops}, Time={iter_time*1000:.6f}ms")
        print(f"Recursive: Result={rec_result}, Calls={rec_calls}, Time={rec_time*1000:.6f}ms")
        
        # Verify results match
        if iter_result == rec_result:
            print(f"✓ Results match!")
        else:
            print(f"✗ Results don't match!")
    
    print("="*70)

def factorial_properties():
    """
    Demonstrate important factorial properties and patterns.
    """
    print("\n" + "="*60)
    print("FACTORIAL PROPERTIES AND PATTERNS")
    print("="*60)
    
    print("1. Factorial values for small numbers:")
    for i in range(0, 11):
        result, _ = factorial_iterative(i)
        print(f"   {i}! = {result}")
    
    print("\n2. Growth rate comparison:")
    print("   n   n!     2^n     n^2")
    print("   -   ----    ----    ----")
    
    for n in range(1, 11):
        fact, _ = factorial_iterative(n)
        power_of_2 = 2 ** n
        square = n ** 2
        print(f"   {n:2d}  {fact:6d}  {power_of_2:6d}  {square:4d}")
    
    print("\n3. Factorial grows faster than exponential!")
    print("="*60)

def factorial_applications():
    """
    Demonstrate practical applications of factorial.
    """
    print("\n" + "="*60)
    print("FACTORIAL APPLICATIONS")
    print("="*60)
    
    # Permutations
    def permutations(n: int, r: int) -> int:
        """Calculate nPr = n! / (n-r)!"""
        if r > n:
            return 0
        numerator, _ = factorial_iterative(n)
        denominator, _ = factorial_iterative(n - r)
        return numerator // denominator
    
    # Combinations
    def combinations(n: int, r: int) -> int:
        """Calculate nCr = n! / (r! × (n-r)!)"""
        if r > n:
            return 0
        numerator, _ = factorial_iterative(n)
        denominator1, _ = factorial_iterative(r)
        denominator2, _ = factorial_iterative(n - r)
        return numerator // (denominator1 * denominator2)
    
    print("1. Permutations (nPr): Number of ways to arrange r items from n")
    n, r = 5, 3
    perm = permutations(n, r)
    print(f"   {n}P{r} = {perm}")
    
    print("\n2. Combinations (nCr): Number of ways to choose r items from n")
    n, r = 5, 3
    comb = combinations(n, r)
    print(f"   {n}C{r} = {comb}")
    
    print("\n3. Pascal's Triangle connection:")
    print("   Row 5: ", end="")
    for r in range(6):
        print(f"{combinations(5, r)} ", end="")
    print()
    
    print("="*60)

def run_comprehensive_tests():
    """
    Run test cases to verify factorial implementations.
    """
    print("\n" + "="*60)
    print("FACTORIAL TEST SUITE")
    print("="*60)
    
    test_cases = [
        (0, 1, "Base case"),
        (1, 1, "1!"),
        (5, 120, "5!"),
        (7, 5040, "7!"),
        (10, 3628800, "10!")
    ]
    
    for n, expected, description in test_cases:
        # Test iterative
        iter_result, iter_ops = factorial_iterative(n)
        iter_status = "[PASS]" if iter_result == expected else "[FAIL]"
        
        # Test recursive
        rec_result, rec_calls = factorial_recursive(n)
        rec_status = "[PASS]" if rec_result == expected else "[FAIL]"
        
        print(f"{iter_status} Iterative {description}: {n}! = {iter_result} ({iter_ops} ops)")
        print(f"{rec_status} Recursive {description}: {n}! = {rec_result} ({rec_calls} calls)")
        print()
    
    print("="*60)

def main():
    """
    Main function to run factorial demonstrations.
    """
    print("Welcome to the Factorial Calculator!")
    print("This program demonstrates both iterative and recursive factorial calculation.")
    
    # Interactive mode
    try:
        n = int(input("\nEnter a non-negative integer to calculate its factorial: "))
        
        if n < 0:
            print("Factorial is not defined for negative numbers!")
        else:
            # Calculate using both methods
            iter_result, iter_ops = factorial_iterative(n)
            rec_result, rec_calls = factorial_recursive(n)
            
            print(f"\nResults:")
            print(f"Iterative: {n}! = {iter_result} ({iter_ops} multiplications)")
            print(f"Recursive: {n}! = {rec_result} ({rec_calls} recursive calls)")
            
            # Show recursive process for smaller numbers
            if n <= 5:
                factorial_recursive_verbose(n)
    
    except ValueError:
        print("Please enter a valid integer!")
    
    # Educational demonstrations
    compare_iterative_recursive()
    factorial_properties()
    factorial_applications()
    run_comprehensive_tests()

if __name__ == "__main__":
    main()
