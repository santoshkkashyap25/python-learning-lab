"""
Collatz Conjecture - The Famous Unsolved Mathematical Problem

The Collatz Conjecture states that for any positive integer n:
- If n is even, divide it by 2 (n → n/2)
- If n is odd, multiply by 3 and add 1 (n → 3n + 1)
- Repeat the process

The conjecture claims that this process will always reach 1, regardless of the starting number.

This remains unproven despite extensive computational verification.
"""

from typing import List, Tuple
import time
import matplotlib.pyplot as plt

def collatz_sequence(n: int) -> Tuple[List[int], int, int]:
    """
    Generate the Collatz sequence for a given starting number.
    
    Args:
        n (int): Positive starting integer
    
    Returns:
        Tuple[List[int], int, int]: A tuple containing:
            - List[int]: The complete Collatz sequence
            - int: Number of steps to reach 1
            - int: Maximum value reached in the sequence
    
    Example:
        >>> collatz_sequence(6)
        ([6, 3, 10, 5, 16, 8, 4, 2, 1], 8, 16)
    """
    if n <= 0:
        raise ValueError("Starting number must be positive")
    
    sequence = [n]
    max_value = n
    steps = 0
    
    while n != 1:
        steps += 1
        
        if n % 2 == 0:  # Even
            n = n // 2
        else:  # Odd
            n = 3 * n + 1
        
        sequence.append(n)
        max_value = max(max_value, n)
    
    return sequence, steps, max_value

def collatz_verbose(n: int) -> None:
    """
    Generate Collatz sequence with detailed step-by-step output.
    
    Args:
        n (int): Positive starting integer
    """
    print("\n" + "="*70)
    print("COLLATZ CONJECTURE - STEP BY STEP")
    print("="*70)
    print(f"Starting number: {n}")
    print("-"*70)
    
    original_n = n
    step = 0
    
    while n != 1:
        step += 1
        
        if n % 2 == 0:
            operation = f"{n} ÷ 2 = {n // 2}"
            n = n // 2
        else:
            operation = f"3 × {n} + 1 = {3 * n + 1}"
            n = 3 * n + 1
        
        print(f"Step {step:2d}: {operation}")
    
    print(f"\nReached 1 after {step} steps!")
    print(f"Total sequence length: {step + 1}")
    print("="*70)

def analyze_collatz_patterns():
    """
    Analyze Collatz sequences for a range of numbers to find patterns.
    """
    print("\n" + "="*70)
    print("COLLATZ PATTERN ANALYSIS")
    print("="*70)
    
    print("Analyzing numbers 1-20:")
    print("n  | Steps | Max Value | Sequence")
    print("-" * 50)
    
    for n in range(1, 21):
        sequence, steps, max_val = collatz_sequence(n)
        
        # Show abbreviated sequence for readability
        if len(sequence) <= 10:
            seq_str = " → ".join(map(str, sequence))
        else:
            seq_str = " → ".join(map(str, sequence[:5])) + " → ... → " + " → ".join(map(str, sequence[-3:]))
        
        print(f"{n:2d} | {steps:5d} | {max_val:8d} | {seq_str}")
    
    print("="*70)

def find_extreme_sequences(limit: int = 1000):
    """
    Find numbers with extreme Collatz sequence properties.
    
    Args:
        limit (int): Upper limit for search (default: 1000)
    """
    print("\n" + "="*70)
    print(f"EXTREME COLLATZ SEQUENCES (1-{limit})")
    print("="*70)
    
    max_steps = 0
    max_steps_num = 0
    max_value = 0
    max_value_num = 0
    
    for n in range(1, limit + 1):
        sequence, steps, max_val = collatz_sequence(n)
        
        if steps > max_steps:
            max_steps = steps
            max_steps_num = n
        
        if max_val > max_value:
            max_value = max_val
            max_value_num = n
    
    print(f"Number with most steps: {max_steps_num} ({max_steps} steps)")
    print(f"Number with highest peak: {max_value_num} (reaches {max_value})")
    
    # Show sequences for extreme cases
    print(f"\nSequence for {max_steps_num} (most steps):")
    seq, steps, max_val = collatz_sequence(max_steps_num)
    print(f"Length: {len(seq)} steps, Peak: {max_val}")
    print(f"Sequence: {' → '.join(map(str, seq[:10]))} → ... → {' → '.join(map(str, seq[-5:]))}")
    
    print(f"\nSequence for {max_value_num} (highest peak):")
    seq, steps, max_val = collatz_sequence(max_value_num)
    print(f"Length: {len(seq)} steps, Peak: {max_val}")
    print(f"Sequence: {' → '.join(map(str, seq[:10]))} → ... → {' → '.join(map(str, seq[-5:]))}")
    
    print("="*70)

def collatz_statistics(limit: int = 100):
    """
    Calculate statistics for Collatz sequences up to a limit.
    
    Args:
        limit (int): Upper limit for analysis (default: 100)
    """
    print("\n" + "="*70)
    print(f"COLLATZ STATISTICS (1-{limit})")
    print("="*70)
    
    total_steps = 0
    step_counts = []
    max_values = []
    
    for n in range(1, limit + 1):
        sequence, steps, max_val = collatz_sequence(n)
        total_steps += steps
        step_counts.append(steps)
        max_values.append(max_val)
    
    avg_steps = total_steps / limit
    max_steps = max(step_counts)
    min_steps = min(step_counts)
    max_overall = max(max_values)
    
    print(f"Total numbers analyzed: {limit}")
    print(f"Average steps to reach 1: {avg_steps:.2f}")
    print(f"Maximum steps: {max_steps}")
    print(f"Minimum steps: {min_steps}")
    print(f"Highest value reached: {max_overall}")
    
    # Distribution of step counts
    print(f"\nStep count distribution:")
    step_ranges = [(0, 10), (11, 20), (21, 50), (51, 100), (101, float('inf'))]
    
    for low, high in step_ranges:
        if high == float('inf'):
            count = sum(1 for steps in step_counts if steps >= low)
            label = f"{low}+"
        else:
            count = sum(1 for steps in step_counts if low <= steps <= high)
            label = f"{low}-{high}"
        
        percentage = (count / limit) * 100
        print(f"  {label:8s} steps: {count:3d} numbers ({percentage:5.1f}%)")
    
    print("="*70)

def verify_conjecture(limit: int = 10000):
    """
    Verify the Collatz conjecture for numbers up to a limit.
    
    Args:
        limit (int): Upper limit for verification (default: 10000)
    """
    print("\n" + "="*70)
    print(f"VERIFYING COLLATZ CONJECTURE (1-{limit})")
    print("="*70)
    
    start_time = time.time()
    failed_numbers = []
    
    for n in range(1, limit + 1):
        try:
            sequence, steps, max_val = collatz_sequence(n)
            if sequence[-1] != 1:
                failed_numbers.append(n)
        except Exception as e:
            failed_numbers.append(n)
            print(f"Error processing {n}: {e}")
    
    end_time = time.time()
    
    if not failed_numbers:
        print(f"✓ Conjecture holds for all numbers from 1 to {limit}")
        print(f"✓ Verification completed in {end_time - start_time:.2f} seconds")
    else:
        print(f"✗ Conjecture failed for numbers: {failed_numbers}")
    
    print("="*70)

def collatz_visualization(n: int):
    """
    Create a simple text-based visualization of the Collatz sequence.
    
    Args:
        n (int): Starting number
    """
    print("\n" + "="*70)
    print(f"COLLATZ SEQUENCE VISUALIZATION FOR {n}")
    print("="*70)
    
    sequence, steps, max_val = collatz_sequence(n)
    
    print(f"Sequence: {' → '.join(map(str, sequence))}")
    print(f"Length: {len(sequence)} steps")
    print(f"Peak value: {max_val}")
    
    # Simple bar chart representation
    print(f"\nSequence visualization (scaled):")
    max_bar_length = 50
    
    for i, value in enumerate(sequence):
        if i % 5 == 0 or i == len(sequence) - 1:  # Show every 5th step and the last
            bar_length = int((value / max_val) * max_bar_length)
            bar = "█" * bar_length
            print(f"Step {i:2d}: {value:8d} |{bar}|")
    
    print("="*70)

def run_comprehensive_tests():
    """
    Run test cases to verify Collatz implementation.
    """
    print("\n" + "="*70)
    print("COLLATZ CONJECTURE TEST SUITE")
    print("="*70)
    
    test_cases = [
        (1, [1], 0, 1, "Base case"),
        (2, [2, 1], 1, 2, "Even number"),
        (3, [3, 10, 5, 16, 8, 4, 2, 1], 7, 16, "Classic example"),
        (6, [6, 3, 10, 5, 16, 8, 4, 2, 1], 8, 16, "Even start"),
        (7, [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 16, 52, "Odd start"),
        (19, [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 20, 52, "Longer sequence")
    ]
    
    for n, expected_seq, expected_steps, expected_max, description in test_cases:
        sequence, steps, max_val = collatz_sequence(n)
        
        seq_correct = sequence == expected_seq
        steps_correct = steps == expected_steps
        max_correct = max_val == expected_max
        
        overall_correct = seq_correct and steps_correct and max_correct
        status = "[PASS]" if overall_correct else "[FAIL]"
        
        print(f"{status} Test: {description} (n={n})")
        print(f"  Steps: {steps} (expected {expected_steps})")
        print(f"  Max value: {max_val} (expected {expected_max})")
        print(f"  Sequence length: {len(sequence)}")
        print()
    
    print("="*70)

def main():
    """
    Main function to run Collatz conjecture demonstrations.
    """
    print("Welcome to the Collatz Conjecture Explorer!")
    print("This program explores the famous unsolved mathematical problem.")
    
    # Interactive mode
    try:
        n = int(input("\nEnter a positive integer to explore its Collatz sequence: "))
        
        if n <= 0:
            print("Please enter a positive integer!")
        else:
            collatz_verbose(n)
            collatz_visualization(n)
    
    except ValueError:
        print("Please enter a valid integer!")
    
    # Educational demonstrations
    analyze_collatz_patterns()
    find_extreme_sequences(100)
    collatz_statistics(50)
    verify_conjecture(1000)
    run_comprehensive_tests()

if __name__ == "__main__":
    main()
