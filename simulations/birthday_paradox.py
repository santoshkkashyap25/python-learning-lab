"""
Birthday Paradox Simulation - Probability of Shared Birthdays

The Birthday Paradox states that in a group of just 23 people, there's a
50% probability that at least two people share the same birthday.
With 70 people, the probability jumps to 99.9%!

This simulation demonstrates this counterintuitive probability concept
through random sampling and mathematical analysis.

Mathematical Formula:
P(no shared birthdays) = (365/365) × (364/365) × (363/365) × ... × ((365-n+1)/365)
P(at least one shared birthday) = 1 - P(no shared birthdays)
"""

from typing import List, Tuple
import random
import datetime
import time
from collections import Counter

class BirthdayParadoxSimulator:
    """Main class for Birthday Paradox simulation and analysis."""
    
    def __init__(self):
        """Initialize the simulator."""
        self.simulation_results = []
        self.leap_year_aware = True
    
    def generate_random_birthday(self, include_leap_year: bool = True) -> datetime.date:
        """
        Generate a random birthday.
        
        Args:
            include_leap_year (bool): Whether to include February 29th
        
        Returns:
            datetime.date: Random birthday date
        """
        # Generate random year (realistic range)
        year = random.randint(1950, 2023)
        
        # Check if leap year
        is_leap = self.is_leap_year(year)
        
        # Generate random month
        month = random.randint(1, 12)
        
        # Generate random day based on month and leap year
        if month == 2:
            if is_leap and include_leap_year:
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        elif month in [4, 6, 9, 11]:  # 30-day months
            day = random.randint(1, 30)
        else:  # 31-day months
            day = random.randint(1, 31)
        
        return datetime.date(year, month, day)
    
    def is_leap_year(self, year: int) -> bool:
        """
        Check if a year is a leap year.
        
        Args:
            year (int): Year to check
        
        Returns:
            bool: True if leap year, False otherwise
        """
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
    
    def simulate_group(self, group_size: int) -> Tuple[bool, List[datetime.date], List[int]]:
        """
        Simulate one group of people and check for shared birthdays.
        
        Args:
            group_size (int): Number of people in the group
        
        Returns:
            Tuple[bool, List[datetime.date], List[int]]: 
                (has_shared_birthday, birthdays, shared_indices)
        """
        birthdays = []
        
        # Generate random birthdays for the group
        for _ in range(group_size):
            birthday = self.generate_random_birthday(self.leap_year_aware)
            birthdays.append(birthday)
        
        # Check for shared birthdays (ignoring year, only month and day)
        month_day_list = [(b.month, b.day) for b in birthdays]
        month_day_counter = Counter(month_day_list)
        
        # Find shared birthdays
        shared_birthdays = [(md, count) for md, count in month_day_counter.items() if count > 1]
        
        if shared_birthdays:
            # Find indices of people with shared birthdays
            shared_indices = []
            for i, (month, day) in enumerate(month_day_list):
                if month_day_counter[(month, day)] > 1:
                    shared_indices.append(i)
            return True, birthdays, shared_indices
        else:
            return False, birthdays, []
    
    def run_multiple_simulations(self, group_size: int, num_simulations: int = 1000) -> Tuple[float, List]:
        """
        Run multiple simulations and calculate probability.
        
        Args:
            group_size (int): Size of each group
            num_simulations (int): Number of simulations to run
        
        Returns:
            Tuple[float, List]: (probability_of_shared_birthday, detailed_results)
        """
        shared_count = 0
        detailed_results = []
        
        print(f"\nRunning {num_simulations} simulations for groups of {group_size} people...")
        
        for i in range(num_simulations):
            has_shared, birthdays, shared_indices = self.simulate_group(group_size)
            
            if has_shared:
                shared_count += 1
            
            detailed_results.append({
                'simulation': i + 1,
                'has_shared': has_shared,
                'birthdays': birthdays,
                'shared_indices': shared_indices
            })
            
            # Progress indicator
            if (i + 1) % 100 == 0:
                print(f"  Completed {i + 1}/{num_simulations} simulations...")
        
        probability = shared_count / num_simulations
        return probability, detailed_results
    
    def calculate_theoretical_probability(self, group_size: int) -> float:
        """
        Calculate the theoretical probability of shared birthdays.
        
        Args:
            group_size (int): Size of the group
        
        Returns:
            float: Theoretical probability (0 to 1)
        """
        if group_size > 366:  # Pigeonhole principle
            return 1.0
        
        # Calculate probability of NO shared birthdays
        prob_no_shared = 1.0
        for i in range(group_size):
            prob_no_shared *= (365 - i) / 365
        
        # Probability of at least one shared birthday
        return 1 - prob_no_shared
    
    def display_simulation_results(self, group_size: int, simulated_prob: float, 
                                 theoretical_prob: float, detailed_results: List) -> None:
        """
        Display comprehensive simulation results.
        
        Args:
            group_size (int): Size of the groups
            simulated_prob (float): Simulated probability
            theoretical_prob (float): Theoretical probability
            detailed_results (List): Detailed simulation results
        """
        print("\n" + "="*70)
        print("BIRTHDAY PARADOX SIMULATION RESULTS")
        print("="*70)
        print(f"Group Size: {group_size} people")
        print(f"Number of Simulations: {len(detailed_results)}")
        print("-"*70)
        print(f"Simulated Probability:     {simulated_prob:.4f} ({simulated_prob*100:.2f}%)")
        print(f"Theoretical Probability:   {theoretical_prob:.4f} ({theoretical_prob*100:.2f}%)")
        print(f"Difference:                {abs(simulated_prob - theoretical_prob):.4f}")
        print("-"*70)
        
        # Analyze shared birthday patterns
        shared_simulations = [r for r in detailed_results if r['has_shared']]
        
        if shared_simulations:
            print(f"\nShared Birthday Analysis:")
            print(f"Simulations with shared birthdays: {len(shared_simulations)}")
            
            # Find example of shared birthday
            example = shared_simulations[0]
            shared_birthdays = example['birthdays']
            shared_indices = example['shared_indices']
            
            print(f"\nExample of shared birthdays:")
            for i in shared_indices:
                birthday = shared_birthdays[i]
                print(f"  Person {i+1}: {birthday.strftime('%B %d')}")
        
        print("="*70)
    
    def demonstrate_probability_curve(self) -> None:
        """
        Demonstrate how probability changes with group size.
        """
        print("\n" + "="*70)
        print("BIRTHDAY PARADOX PROBABILITY CURVE")
        print("="*70)
        print("Group Size | Theoretical | Simulated | Difference")
        print("-"*70)
        
        group_sizes = [2, 5, 10, 15, 20, 22, 23, 30, 40, 50, 60, 70]
        
        for size in group_sizes:
            theoretical = self.calculate_theoretical_probability(size)
            simulated, _ = self.run_multiple_simulations(size, 1000)
            difference = abs(theoretical - simulated)
            
            print(f"{size:10d} | {theoretical:11.4f} | {simulated:9.4f} | {difference:10.4f}")
        
        print("="*70)
    
    def find_break_even_point(self) -> None:
        """
        Find the group size where probability exceeds 50%.
        """
        print("\n" + "="*70)
        print("FINDING 50% PROBABILITY POINT")
        print("="*70)
        
        for size in range(2, 60):
            prob = self.calculate_theoretical_probability(size)
            if prob >= 0.5:
                print(f"Theoretical 50% point: {size} people ({prob:.4f} = {prob*100:.2f}%)")
                
                # Verify with simulation
                sim_prob, _ = self.run_multiple_simulations(size, 5000)
                print(f"Simulated probability:   {sim_prob:.4f} = {sim_prob*100:.2f}%")
                break
        
        print("="*70)
    
    def interactive_simulation(self) -> None:
        """
        Run an interactive simulation with user input.
        """
        print("\n" + "="*70)
        print("INTERACTIVE BIRTHDAY PARADOX SIMULATION")
        print("="*70)
        
        try:
            group_size = int(input("Enter group size (2-100): "))
            if group_size < 2 or group_size > 100:
                print("Please enter a group size between 2 and 100.")
                return
            
            num_simulations = int(input("Enter number of simulations (100-10000): "))
            if num_simulations < 100 or num_simulations > 10000:
                print("Please enter between 100 and 10000 simulations.")
                return
            
            # Run simulation
            simulated_prob, detailed_results = self.run_multiple_simulations(group_size, num_simulations)
            theoretical_prob = self.calculate_theoretical_probability(group_size)
            
            # Display results
            self.display_simulation_results(group_size, simulated_prob, theoretical_prob, detailed_results)
            
        except ValueError:
            print("Please enter valid numbers.")
    
    def explain_the_paradox(self) -> None:
        """
        Explain why the birthday paradox seems counterintuitive.
        """
        print("\n" + "="*70)
        print("WHY THE BIRTHDAY PARADOX SEEMS SURPRISING")
        print("="*70)
        
        print("The Birthday Paradox seems counterintuitive because:")
        print()
        print("1. ❌ COMMON MISCONCEPTION:")
        print("   People think: 'What's the chance someone has MY birthday?'")
        print("   This probability is indeed low: 1/365 ≈ 0.27%")
        print()
        print("2. ✅ ACTUAL QUESTION:")
        print("   We're asking: 'What's the chance ANY TWO people share ANY birthday?'")
        print()
        print("3. 📊 COMBINATORIAL EXPLOSION:")
        print("   With n people, there are n×(n-1)/2 possible pairs:")
        print("   • 23 people → 253 pairs")
        print("   • 50 people → 1,225 pairs")
        print("   • 70 people → 2,415 pairs")
        print()
        print("4. 🎯 PROBABILITY ACCUMULATION:")
        print("   Each pair has a 1/365 chance of matching")
        print("   With 253 pairs, the cumulative probability becomes significant!")
        print()
        print("5. 📈 THE CURVE:")
        print("   • 10 people: 11.9% chance")
        print("   • 20 people: 41.1% chance")
        print("   • 23 people: 50.7% chance ← The famous '23 people' result")
        print("   • 30 people: 70.6% chance")
        print("   • 50 people: 97.0% chance")
        print("   • 70 people: 99.9% chance")
        
        print("="*70)
    
    def run_original_demo(self) -> None:
        """
        Run the original demonstration from the base code.
        """
        print("\n" + "="*70)
        print("ORIGINAL DEMONSTRATION (50 RANDOM BIRTHDAYS)")
        print("="*70)
        
        birthdays = []
        
        # Generate 50 random birthdays (like original code)
        for i in range(50):
            year = random.randint(1895, 2017)
            birthday = self.generate_random_birthday(self.leap_year_aware)
            day_of_year = birthday.timetuple().tm_yday
            birthdays.append(day_of_year)
        
        birthdays.sort()
        
        print("Generated 50 random birthdays (day of year):")
        for i, birthday in enumerate(birthdays):
            print(f"{i+1:2d}: Day {birthday:3d}")
        
        # Check for duplicates
        birthday_counts = Counter(birthdays)
        duplicates = [(day, count) for day, count in birthday_counts.items() if count > 1]
        
        if duplicates:
            print(f"\n🎉 Found {len(duplicates)} shared birthday(s)!")
            for day, count in duplicates:
                print(f"   Day {day}: {count} people")
        else:
            print("\n❌ No shared birthdays found in this group.")
        
        theoretical_prob = self.calculate_theoretical_probability(50)
        print(f"\nTheoretical probability for 50 people: {theoretical_prob:.4f} ({theoretical_prob*100:.2f}%)")
        
        print("="*70)

def main():
    """Main function to run the Birthday Paradox simulator."""
    print("🎂 Welcome to the Birthday Paradox Simulator! 🎂")
    print("Explore this fascinating probability puzzle!")
    
    simulator = BirthdayParadoxSimulator()
    
    while True:
        print("\n" + "="*70)
        print("🎂 BIRTHDAY PARADOX SIMULATOR MENU")
        print("="*70)
        print("1. 🎯 Interactive Simulation")
        print("2. 📊 Probability Curve Demonstration")
        print("3. 🔍 Find 50% Probability Point")
        print("4. 📚 Explain the Paradox")
        print("5. 🎲 Original Demo (50 birthdays)")
        print("6. 🚪 Quit")
        print("="*70)
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            simulator.interactive_simulation()
        elif choice == "2":
            simulator.demonstrate_probability_curve()
        elif choice == "3":
            simulator.find_break_even_point()
        elif choice == "4":
            simulator.explain_the_paradox()
        elif choice == "5":
            simulator.run_original_demo()
        elif choice == "6":
            print("Thanks for exploring the Birthday Paradox! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
