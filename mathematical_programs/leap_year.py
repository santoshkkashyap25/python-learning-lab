"""
Leap Year Calculator - Determining Leap Years

A leap year is a year that contains an extra day (February 29th) to keep the
calendar year synchronized with the astronomical year.

Rules for determining leap years:
1. If the year is divisible by 400, it's a leap year
2. If the year is divisible by 100 but not by 400, it's NOT a leap year
3. If the year is divisible by 4 but not by 100, it's a leap year
4. Otherwise, it's NOT a leap year

This means: Leap years are years divisible by 4, except for century years
not divisible by 400.
"""

from typing import List, Tuple
import random
import datetime

def is_leap_year(year: int) -> Tuple[bool, str]:
    """
    Determine if a given year is a leap year.
    
    Args:
        year (int): Year to check (positive integer)
    
    Returns:
        Tuple[bool, str]: A tuple containing:
            - bool: True if leap year, False otherwise
            - str: Explanation of why it is/isn't a leap year
    
    Example:
        >>> is_leap_year(2020)
        (True, "2020 is divisible by 4 and not a century year - Leap year!")
        
        >>> is_leap_year(1900)
        (False, "1900 is divisible by 100 but not by 400 - Not a leap year!")
    """
    if year % 400 == 0:
        return True, f"{year} is divisible by 400 - Leap year!"
    elif year % 100 == 0:
        return False, f"{year} is divisible by 100 but not by 400 - Not a leap year!"
    elif year % 4 == 0:
        return True, f"{year} is divisible by 4 and not a century year - Leap year!"
    else:
        return False, f"{year} is not divisible by 4 - Not a leap year!"

def is_leap_year_simple(year: int) -> bool:
    """
    Simple leap year check returning only boolean.
    
    Args:
        year (int): Year to check
    
    Returns:
        bool: True if leap year, False otherwise
    """
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def leap_year_verbose(year: int) -> None:
    """
    Detailed leap year analysis with step-by-step explanation.
    
    Args:
        year (int): Year to analyze
    """
    print("\n" + "="*60)
    print("LEAP YEAR ANALYSIS")
    print("="*60)
    print(f"Analyzing year: {year}")
    print("-"*60)
    
    print(f"Step 1: Check if {year} is divisible by 400")
    if year % 400 == 0:
        print(f"  {year} ÷ 400 = {year // 400} (no remainder)")
        print(f"  ✓ {year} is divisible by 400")
        print(f"  → {year} IS a leap year!")
        print("="*60)
        return
    else:
        print(f"  {year} ÷ 400 = {year // 400} remainder {year % 400}")
        print(f"  ✗ {year} is NOT divisible by 400")
    
    print(f"\nStep 2: Check if {year} is divisible by 100")
    if year % 100 == 0:
        print(f"  {year} ÷ 100 = {year // 100} (no remainder)")
        print(f"  ✓ {year} is divisible by 100")
        print(f"  → Since {year} is not divisible by 400, it's NOT a leap year!")
        print("="*60)
        return
    else:
        print(f"  {year} ÷ 100 = {year // 100} remainder {year % 100}")
        print(f"  ✗ {year} is NOT divisible by 100")
    
    print(f"\nStep 3: Check if {year} is divisible by 4")
    if year % 4 == 0:
        print(f"  {year} ÷ 4 = {year // 4} (no remainder)")
        print(f"  ✓ {year} is divisible by 4")
        print(f"  → {year} IS a leap year!")
    else:
        print(f"  {year} ÷ 4 = {year // 4} remainder {year % 4}")
        print(f"  ✗ {year} is NOT divisible by 4")
        print(f"  → {year} is NOT a leap year!")
    
    print("="*60)

def analyze_year_range(start_year: int, end_year: int) -> None:
    """
    Analyze leap years in a given range.
    
    Args:
        start_year (int): Start year (inclusive)
        end_year (int): End year (inclusive)
    """
    print("\n" + "="*70)
    print(f"LEAP YEAR ANALYSIS FOR {start_year}-{end_year}")
    print("="*70)
    
    leap_years = []
    non_leap_years = []
    
    for year in range(start_year, end_year + 1):
        is_leap, explanation = is_leap_year(year)
        
        if is_leap:
            leap_years.append(year)
        else:
            non_leap_years.append(year)
    
    print(f"Total years analyzed: {end_year - start_year + 1}")
    print(f"Leap years: {len(leap_years)}")
    print(f"Non-leap years: {len(non_leap_years)}")
    print(f"Leap year percentage: {(len(leap_years) / (end_year - start_year + 1)) * 100:.1f}%")
    
    print(f"\nLeap years in this range:")
    for i, year in enumerate(leap_years):
        if i % 10 == 0 and i > 0:
            print()
        print(f"{year:4d}", end=" ")
    print("\n")
    
    # Show some interesting patterns
    print(f"\nInteresting patterns:")
    print(f"- Leap years occur every 4 years, except...")
    print(f"- Century years (ending in 00) are only leap years if divisible by 400")
    
    century_years = [year for year in range(start_year, end_year + 1) if year % 100 == 0]
    leap_century_years = [year for year in century_years if year % 400 == 0]
    
    if century_years:
        print(f"\nCentury years in range ({start_year}-{end_year}):")
        for year in century_years:
            is_leap, _ = is_leap_year(year)
            status = "Leap" if is_leap else "Not leap"
            print(f"  {year}: {status}")
    
    print("="*70)

def leap_year_calendar_info(year: int) -> None:
    """
    Provide calendar information about a leap year.
    
    Args:
        year (int): Year to analyze
    """
    print("\n" + "="*60)
    print(f"CALENDAR INFORMATION FOR {year}")
    print("="*60)
    
    is_leap, explanation = is_leap_year(year)
    print(f"Leap year status: {explanation}")
    
    if is_leap:
        print(f"\nSpecial dates in {year}:")
        print(f"- February has 29 days (instead of 28)")
        print(f"- Total days in year: 366 (instead of 365)")
        print(f"- Day of week for Feb 29: {datetime.date(year, 2, 29).strftime('%A')}")
        
        # Calculate day of year for Dec 31
        day_of_year = datetime.date(year, 12, 31).timetuple().tm_yday
        print(f"- December 31 is the {day_of_year}th day of the year")
    else:
        print(f"\nStandard year information:")
        print(f"- February has 28 days")
        print(f"- Total days in year: 365")
        print(f"- Day of year for Dec 31: 365")
    
    # Show what day of week the year starts and ends
    start_day = datetime.date(year, 1, 1).strftime("%A")
    end_day = datetime.date(year, 12, 31).strftime("%A")
    print(f"- Year starts on: {start_day}")
    print(f"- Year ends on: {end_day}")
    
    print("="*60)

def leap_year_trivia():
    """
    Display interesting leap year facts and trivia.
    """
    print("\n" + "="*60)
    print("LEAP YEAR TRIVIA AND FACTS")
    print("="*60)
    
    facts = [
        "The concept of leap years was introduced by Julius Caesar in 45 BCE",
        "The Gregorian calendar (our current system) was introduced in 1582",
        "The average year length is 365.2425 days (with leap years)",
        "Without leap years, the calendar would drift by about 1 day every 4 years",
        "People born on February 29 are called 'leaplings' or 'leapers'",
        "The probability of being born on Feb 29 is 1 in 1,461",
        "2000 was a leap year (divisible by 400), but 1900 was not",
        "2100 will not be a leap year (century year not divisible by 400)",
        "The next skipped leap year will be 2100",
        "Some countries have special traditions for leap day proposals"
    ]
    
    for i, fact in enumerate(facts, 1):
        print(f"{i:2d}. {fact}")
    
    print("="*60)

def run_comprehensive_tests():
    """
    Run test cases to verify leap year implementation.
    """
    print("\n" + "="*60)
    print("LEAP YEAR TEST SUITE")
    print("="*60)
    
    test_cases = [
        (2000, True, "Divisible by 400"),
        (1900, False, "Century year not divisible by 400"),
        (2020, True, "Recent leap year"),
        (2021, False, "Recent non-leap year"),
        (2024, True, "Future leap year"),
        (2100, False, "Future century year"),
        (4, True, "Small leap year"),
        (1, False, "Small non-leap year"),
        (1600, True, "Historical leap year"),
        (1700, False, "Historical non-leap century year")
    ]
    
    for year, expected, description in test_cases:
        is_leap, explanation = is_leap_year(year)
        status = "[PASS]" if is_leap == expected else "[FAIL]"
        
        print(f"{status} {description}: {year}")
        print(f"  Result: {explanation}")
        print()
    
    print("="*60)

def leap_year_probability_simulation():
    """
    Simulate the probability of randomly selecting a leap year.
    """
    print("\n" + "="*60)
    print("LEAP YEAR PROBABILITY SIMULATION")
    print("="*60)
    
    # Mathematical probability
    # In 400-year cycle: 97 leap years, 303 non-leap years
    theoretical_prob = 97 / 400
    print(f"Theoretical probability: {theoretical_prob:.4f} ({theoretical_prob*100:.2f}%)")
    
    # Simulation
    import random
    num_trials = 100000
    leap_count = 0
    
    for _ in range(num_trials):
        year = random.randint(1, 400)  # One complete cycle
        if is_leap_year_simple(year):
            leap_count += 1
    
    simulated_prob = leap_count / num_trials
    print(f"Simulated probability:  {simulated_prob:.4f} ({simulated_prob*100:.2f}%)")
    print(f"Difference: {abs(theoretical_prob - simulated_prob):.6f}")
    print("="*60)

def main():
    """
    Main function to run leap year demonstrations.
    """
    print("Welcome to the Leap Year Calculator!")
    print("This program explores the fascinating rules behind leap years.")
    
    # Interactive mode
    try:
        year = int(input("\nEnter a year to check if it's a leap year: "))
        
        if year <= 0:
            print("Please enter a positive year!")
        else:
            leap_year_verbose(year)
            leap_year_calendar_info(year)
    
    except ValueError:
        print("Please enter a valid year!")
    
    # Random year demonstration (from original code)
    random_year = random.randint(1993, 2020)
    print(f"\nRandom year demonstration (like original code):")
    print(f"Year: {random_year}")
    is_leap, explanation = is_leap_year(random_year)
    print(f"Result: {explanation}")
    
    # Educational demonstrations
    analyze_year_range(1990, 2030)
    leap_year_trivia()
    run_comprehensive_tests()
    leap_year_probability_simulation()

if __name__ == "__main__":
    main()
