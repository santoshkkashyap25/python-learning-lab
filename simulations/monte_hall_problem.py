"""
Monte Hall Problem - The Famous Probability Puzzle

The Monte Hall Problem is a probability puzzle based on the American game show
"Let's Make a Deal." Here's the scenario:

1. There are 3 doors. Behind one door is a car (prize), behind the other two are goats.
2. You pick one door.
3. The host (who knows what's behind the doors) opens one of the remaining doors,
   always revealing a goat.
4. You're given the choice to either stick with your original choice or switch to the
   remaining unopened door.
5. Should you switch?

The surprising answer: YES! Switching gives you a 2/3 chance of winning, while
sticking gives you only a 1/3 chance.

This simulation demonstrates and explains this counterintuitive result.
"""

from typing import List, Tuple, Dict
import random
import time

class MonteHallSimulator:
    """Main class for Monte Hall Problem simulation and analysis."""
    
    def __init__(self):
        """Initialize the simulator."""
        self.simulation_history = []
        self.total_switch_wins = 0
        self.total_stay_wins = 0
        self.total_games = 0
    
    def setup_game(self) -> Tuple[int, List[int]]:
        """
        Set up a new game with random prize placement.
        
        Returns:
            Tuple[int, List[int]]: (prize_door, all_doors)
        """
        doors = [0, 1, 2]  # Three doors
        prize_door = random.choice(doors)
        return prize_door, doors
    
    def host_opens_door(self, prize_door: int, player_choice: int) -> int:
        """
        Host opens a door revealing a goat.
        
        Args:
            prize_door (int): Door with the car
            player_choice (int): Door initially chosen by player
        
        Returns:
            int: Door opened by host
        """
        available_doors = [0, 1, 2]
        available_doors.remove(player_choice)
        
        # Host never opens the prize door
        if prize_door in available_doors:
            available_doors.remove(prize_door)
        
        # Host opens one of the remaining doors (both have goats)
        host_door = random.choice(available_doors)
        return host_door
    
    def play_game(self, switch: bool = False, verbose: bool = False) -> Tuple[bool, Dict]:
        """
        Play one round of the Monte Hall game.
        
        Args:
            switch (bool): Whether player switches their choice
            verbose (bool): Whether to show detailed output
        
        Returns:
            Tuple[bool, Dict]: (won, game_details)
        """
        # Set up game
        prize_door, doors = self.setup_game()
        
        # Player makes initial choice
        player_choice = random.choice(doors)
        
        # Host opens a door
        host_door = self.host_opens_door(prize_door, player_choice)
        
        # Remaining door for switching
        remaining_door = [door for door in doors if door not in [player_choice, host_door]][0]
        
        # Player's final choice
        if switch:
            final_choice = remaining_door
        else:
            final_choice = player_choice
        
        # Determine if player won
        won = (final_choice == prize_door)
        
        # Game details for analysis
        game_details = {
            'prize_door': prize_door,
            'initial_choice': player_choice,
            'host_door': host_door,
            'remaining_door': remaining_door,
            'final_choice': final_choice,
            'switched': switch,
            'won': won
        }
        
        if verbose:
            self.display_game_details(game_details)
        
        # Update statistics
        self.total_games += 1
        if switch:
            if won:
                self.total_switch_wins += 1
        else:
            if won:
                self.total_stay_wins += 1
        
        return won, game_details
    
    def display_game_details(self, details: Dict) -> None:
        """
        Display detailed information about one game.
        
        Args:
            details (Dict): Game details dictionary
        """
        print("\n" + "="*50)
        print("GAME DETAILS")
        print("="*50)
        print(f"Prize behind door: {details['prize_door']}")
        print(f"Your initial choice: {details['initial_choice']}")
        print(f"Host opened door: {details['host_door']} (goat)")
        print(f"Remaining door: {details['remaining_door']}")
        print(f"You {'switched' if details['switched'] else 'stayed'} with door {details['final_choice']}")
        
        if details['won']:
            print("🎉 YOU WON THE CAR! 🎉")
        else:
            print("🐐 You got a goat! 🐐")
        
        print("="*50)
    
    def run_simulation(self, num_games: int, switch: bool = False) -> Tuple[int, float]:
        """
        Run multiple games and calculate win rate.
        
        Args:
            num_games (int): Number of games to simulate
            switch (bool): Whether to switch in each game
        
        Returns:
            Tuple[int, float]: (wins, win_percentage)
        """
        wins = 0
        
        print(f"\nRunning {num_games} simulations (switch={'Yes' if switch else 'No'})...")
        
        for i in range(num_games):
            won, _ = self.play_game(switch=switch)
            if won:
                wins += 1
            
            # Progress indicator
            if (i + 1) % 100 == 0:
                print(f"  Completed {i + 1}/{num_games} games...")
        
        win_percentage = (wins / num_games) * 100
        return wins, win_percentage
    
    def compare_strategies(self, num_games: int = 1000) -> None:
        """
        Compare switching vs staying strategies.
        
        Args:
            num_games (int): Number of games for each strategy
        """
        print("\n" + "="*70)
        print("COMPARING STRATEGIES: SWITCH vs STAY")
        print("="*70)
        
        # Test switching strategy
        switch_wins, switch_percentage = self.run_simulation(num_games, switch=True)
        
        # Test staying strategy
        stay_wins, stay_percentage = self.run_simulation(num_games, switch=False)
        
        print("\n" + "="*70)
        print("RESULTS")
        print("="*70)
        print(f"Games per strategy: {num_games}")
        print("-"*70)
        print(f"Always SWITCH: {switch_wins} wins ({switch_percentage:.1f}%)")
        print(f"Always STAY:   {stay_wins} wins ({stay_percentage:.1f}%)")
        print("-"*70)
        
        if switch_percentage > stay_percentage:
            improvement = switch_percentage - stay_percentage
            print(f"✅ Switching is better by {improvement:.1f}%!")
        else:
            print("❌ Unexpected result - staying performed better")
        
        print("="*70)
    
    def interactive_game(self) -> None:
        """
        Play an interactive game with the user.
        """
        print("\n" + "="*70)
        print("🎮 INTERACTIVE MONTE HALL GAME")
        print("="*70)
        print("Welcome to 'Let's Make a Deal'!")
        print("There are 3 doors. Behind one is a car, behind the others are goats.")
        print("-"*70)
        
        # Set up game
        prize_door, doors = self.setup_game()
        
        # Player chooses
        while True:
            try:
                choice = int(input("Choose a door (1, 2, or 3): ")) - 1
                if choice in doors:
                    break
                else:
                    print("Please choose 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        print(f"\nYou chose door {choice + 1}.")
        
        # Host opens a door
        host_door = self.host_opens_door(prize_door, choice)
        print(f"The host opens door {host_door + 1} to reveal a goat!")
        
        # Remaining door
        remaining_door = [door for door in doors if door not in [choice, host_door]][0]
        print(f"Door {remaining_door + 1} remains closed.")
        
        # Player decides to switch or stay
        while True:
            switch_choice = input(f"Do you want to switch to door {remaining_door + 1}? (y/n): ").lower()
            if switch_choice in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")
        
        final_choice = remaining_door if switch_choice == 'y' else choice
        switched = (switch_choice == 'y')
        
        print(f"\nYou {'switched to' if switched else 'stayed with'} door {final_choice + 1}.")
        print("Let's see what's behind your door...")
        time.sleep(2)
        
        # Reveal result
        if final_choice == prize_door:
            print(f"\n🎉 CONGRATULATIONS! You won the car! 🎉")
            print(f"The car was behind door {prize_door + 1}.")
        else:
            print(f"\n🐐 Sorry! You got a goat! 🐐")
            print(f"The car was behind door {prize_door + 1}.")
        
        # Update statistics
        self.total_games += 1
        if switched:
            if final_choice == prize_door:
                self.total_switch_wins += 1
        else:
            if final_choice == prize_door:
                self.total_stay_wins += 1
    
    def explain_the_solution(self) -> None:
        """
        Explain why switching is the optimal strategy.
        """
        print("\n" + "="*70)
        print("🧠 WHY SWITCHING WORKS: THE MATHEMATICAL EXPLANATION")
        print("="*70)
        
        print("📊 INITIAL PROBABILITIES:")
        print("• You pick door 1 (any door works the same)")
        print("• P(Car behind door 1) = 1/3")
        print("• P(Car behind doors 2 or 3) = 2/3")
        print()
        
        print("🚪 HOST'S ACTION:")
        print("• Host KNOWS where the car is")
        print("• Host ALWAYS opens a door with a goat")
        print("• Host's action provides NEW INFORMATION")
        print()
        
        print("🔄 THE KEY INSIGHT:")
        print("• If you initially picked a goat (2/3 probability):")
        print("  - Host must open the OTHER goat door")
        print("  - The remaining door MUST have the car")
        print("  - Switching wins!")
        print()
        print("• If you initially picked the car (1/3 probability):")
        print("  - Host opens either goat door")
        print("  - The remaining door has a goat")
        print("  - Switching loses!")
        print()
        
        print("📈 FINAL PROBABILITIES:")
        print("• P(Win by switching) = 2/3 ≈ 66.7%")
        print("• P(Win by staying)   = 1/3 ≈ 33.3%")
        print()
        
        print("🎯 INTUITION CHECK:")
        print("Imagine 100 doors instead of 3:")
        print("• You pick one door (1% chance of being right)")
        print("• Host opens 98 doors, all showing goats")
        print("• Only one other door remains closed")
        print("• Would you switch? (Hint: YES! 99% vs 1%)")
        
        print("="*70)
    
    def demonstrate_all_scenarios(self) -> None:
        """
        Demonstrate all possible scenarios in the game.
        """
        print("\n" + "="*70)
        print("🔍 ALL POSSIBLE SCENARIOS")
        print("="*70)
        
        scenarios = []
        
        # Generate all possible scenarios
        for prize_door in [0, 1, 2]:
            for initial_choice in [0, 1, 2]:
                # Determine what host opens
                available_doors = [0, 1, 2]
                available_doors.remove(initial_choice)
                
                if prize_door in available_doors:
                    available_doors.remove(prize_door)
                
                host_door = random.choice(available_doors)
                remaining_door = [d for d in [0, 1, 2] if d not in [initial_choice, host_door]][0]
                
                # Results for both strategies
                stay_wins = (initial_choice == prize_door)
                switch_wins = (remaining_door == prize_door)
                
                scenarios.append({
                    'prize': prize_door,
                    'initial': initial_choice,
                    'host': host_door,
                    'remaining': remaining_door,
                    'stay_wins': stay_wins,
                    'switch_wins': switch_wins
                })
        
        # Group by initial choice
        for initial in [0, 1, 2]:
            initial_scenarios = [s for s in scenarios if s['initial'] == initial]
            print(f"\nIf you initially choose door {initial + 1}:")
            print("-" * 50)
            
            stay_wins = sum(1 for s in initial_scenarios if s['stay_wins'])
            switch_wins = sum(1 for s in initial_scenarios if s['switch_wins'])
            
            print(f"Stay wins: {stay_wins}/3 cases")
            print(f"Switch wins: {switch_wins}/3 cases")
            
            for scenario in initial_scenarios:
                prize_door = scenario['prize']
                host_door = scenario['host']
                remaining = scenario['remaining']
                
                stay_result = "WIN" if scenario['stay_wins'] else "LOSE"
                switch_result = "WIN" if scenario['switch_wins'] else "LOSE"
                
                print(f"  Car behind {prize_door + 1}: Host opens {host_door + 1}, "
                      f"Stay={stay_result}, Switch={switch_result}")
        
        print("\n" + "="*70)
        print("SUMMARY:")
        print("• Stay wins in 1 out of 3 scenarios (33.3%)")
        print("• Switch wins in 2 out of 3 scenarios (66.7%)")
        print("="*70)
    
    def display_statistics(self) -> None:
        """Display cumulative statistics from all games played."""
        print("\n" + "="*70)
        print("📊 CUMULATIVE STATISTICS")
        print("="*70)
        print(f"Total games played: {self.total_games}")
        
        if self.total_games > 0:
            switch_games = self.total_games - self.total_stay_wins - (self.total_switch_wins if self.total_switch_wins > 0 else 0)
            
            print(f"Switch strategy wins: {self.total_switch_wins}")
            print(f"Stay strategy wins: {self.total_stay_wins}")
            
            if self.total_switch_wins > 0:
                switch_rate = (self.total_switch_wins / (self.total_switch_wins + (self.total_games - self.total_switch_wins - self.total_stay_wins))) * 100
                print(f"Switch win rate: {switch_rate:.1f}%")
            
            if self.total_stay_wins > 0:
                stay_rate = (self.total_stay_wins / (self.total_stay_wins + (self.total_games - self.total_switch_wins - self.total_stay_wins))) * 100
                print(f"Stay win rate: {stay_rate:.1f}%")
        
        print("="*70)

def main():
    """Main function to run the Monte Hall Problem simulator."""
    print("🚗 Welcome to the Monte Hall Problem Simulator! 🐐")
    print("Explore this famous probability puzzle!")
    
    simulator = MonteHallSimulator()
    
    while True:
        print("\n" + "="*70)
        print("🚗 MONTE HALL PROBLEM SIMULATOR MENU")
        print("="*70)
        print("1. 🎮 Play Interactive Game")
        print("2. 📊 Compare Strategies (1000 games)")
        print("3. 🧠 Mathematical Explanation")
        print("4. 🔍 Analyze All Scenarios")
        print("5. 📈 Custom Simulation")
        print("6. 📊 View Statistics")
        print("7. 🚪 Quit")
        print("="*70)
        
        choice = input("Select an option (1-7): ").strip()
        
        if choice == "1":
            simulator.interactive_game()
        elif choice == "2":
            simulator.compare_strategies(1000)
        elif choice == "3":
            simulator.explain_the_solution()
        elif choice == "4":
            simulator.demonstrate_all_scenarios()
        elif choice == "5":
            try:
                num_games = int(input("Enter number of games to simulate (100-10000): "))
                if 100 <= num_games <= 10000:
                    simulator.compare_strategies(num_games)
                else:
                    print("Please enter a number between 100 and 10000.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            simulator.display_statistics()
        elif choice == "7":
            print("Thanks for exploring the Monte Hall Problem! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
