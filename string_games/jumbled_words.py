"""
Jumbled Words Game - Interactive Word Puzzle Game

A fun two-player game where players take turns unscrambling jumbled words.
The game features a scoring system, hints, and various difficulty levels.

Features:
- Two-player support with score tracking
- Multiple word categories
- Difficulty levels
- Hint system
- Statistics tracking
"""

from typing import List, Tuple, Dict
import random
import time

class JumbledWordsGame:
    """Main class for the Jumbled Words game."""
    
    def __init__(self):
        """Initialize the game with word categories and game state."""
        self.word_categories = {
            "Technology": [
                "COMPUTER", "PROGRAM", "COMPUTING", "INTELLIGENCE", "MEMORY",
                "POWERPOINT", "DATABASE", "DATA", "ANALOGUE", "DIGITAL",
                "SIGNAL", "BLOCK", "CODER", "DECODER", "TRANSISTOR",
                "SYSTEM", "SCHEDULE", "ACCESS", "CACHE", "COOKIES",
                "SIMULATION", "UBUNTU", "TELEVISION", "MOBILE", "SCIENCE",
                "LOGIC", "ANALYTIC", "MENTAL", "ABILITY", "TIME",
                "NETWORK", "GENERAL", "PUBLIC", "INTERNET", "INTRANET",
                "WIRELESS", "REMOTE", "PROCESS", "THREAD", "THEORY",
                "LEMMA", "AXIOM", "CABLE", "OPERATING", "WEB", "STORAGE"
            ],
            "Animals": [
                "ELEPHANT", "GIRAFFE", "PENGUIN", "DOLPHIN", "BUTTERFLY",
                "CROCODILE", "KANGAROO", "OCTOPUS", "TIGER", "LION",
                "MONKEY", "ZEBRA", "EAGLE", "SNAKE", "TURTLE"
            ],
            "Countries": [
                "AMERICA", "BRAZIL", "CANADA", "DENMARK", "EGYPT",
                "FRANCE", "GERMANY", "INDIA", "JAPAN", "KENYA",
                "MEXICO", "NORWAY", "PORTUGAL", "RUSSIA", "SPAIN"
            ],
            "Easy": [
                "CAT", "DOG", "SUN", "MOON", "STAR", "TREE", "BOOK",
                "DESK", "DOOR", "WALL", "BALL", "GAME", "FOOD", "FISH"
            ]
        }
        
        self.current_category = "Technology"
        self.difficulty = "Medium"
        self.hints_enabled = True
        self.game_history = []
    
    def choose_word(self, category: str = None) -> str:
        """
        Choose a random word from the specified category.
        
        Args:
            category (str): Category to choose from (default: current category)
        
        Returns:
            str: Selected word
        """
        if category is None:
            category = self.current_category
        
        words = self.word_categories.get(category, self.word_categories["Technology"])
        return random.choice(words)
    
    def jumble_word(self, word: str) -> str:
        """
        Jumble the letters of a word.
        
        Args:
            word (str): Word to jumble
        
        Returns:
            str: Jumbled word
        """
        # Ensure the jumbled word is different from the original
        jumbled = word
        attempts = 0
        
        while jumbled == word and attempts < 10:
            jumbled = "".join(random.sample(word, len(word)))
            attempts += 1
        
        return jumbled
    
    def calculate_score(self, word_length: int, time_taken: float, hints_used: int) -> int:
        """
        Calculate score based on word length, time, and hints used.
        
        Args:
            word_length (int): Length of the word
            time_taken (float): Time taken to solve (seconds)
            hints_used (int): Number of hints used
        
        Returns:
            int: Calculated score
        """
        base_score = word_length * 2
        
        # Time bonus (faster = more points)
        if time_taken < 10:
            time_bonus = 10
        elif time_taken < 30:
            time_bonus = 5
        else:
            time_bonus = 0
        
        # Hint penalty
        hint_penalty = hints_used * 3
        
        total_score = base_score + time_bonus - hint_penalty
        return max(total_score, 1)  # Minimum 1 point
    
    def get_hint(self, word: str, hint_number: int) -> str:
        """
        Provide hints for the word.
        
        Args:
            word (str): The actual word
            hint_number (int): Which hint to provide (1, 2, or 3)
        
        Returns:
            str: Hint text
        """
        if hint_number == 1:
            return f"Hint 1: The word has {len(word)} letters."
        elif hint_number == 2:
            return f"Hint 2: The word starts with '{word[0]}' and ends with '{word[-1]}'."
        elif hint_number == 3:
            middle = word[1:-1] if len(word) > 2 else ""
            return f"Hint 3: The middle letters are '{middle}'."
        else:
            return "No more hints available!"
    
    def display_categories(self) -> None:
        """Display available word categories."""
        print("\n" + "="*50)
        print("WORD CATEGORIES")
        print("="*50)
        for i, category in enumerate(self.word_categories.keys(), 1):
            word_count = len(self.word_categories[category])
            print(f"{i}. {category} ({word_count} words)")
        print("="*50)
    
    def select_category(self) -> str:
        """
        Let players select a word category.
        
        Returns:
            str: Selected category name
        """
        self.display_categories()
        
        while True:
            try:
                choice = int(input("\nSelect a category (enter number): "))
                categories = list(self.word_categories.keys())
                
                if 1 <= choice <= len(categories):
                    selected = categories[choice - 1]
                    print(f"Selected category: {selected}")
                    return selected
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def play_round(self, player_name: str) -> Tuple[int, bool]:
        """
        Play one round of the game.
        
        Args:
            player_name (str): Name of the current player
        
        Returns:
            Tuple[int, bool]: (score earned, whether the answer was correct)
        """
        # Choose and jumble word
        word = self.choose_word()
        jumbled = self.jumble_word(word)
        
        print(f"\n{'='*50}")
        print(f"{player_name}'s Turn")
        print(f"{'='*50}")
        print(f"Category: {self.current_category}")
        print(f"Jumbled word: {jumbled}")
        
        # Track time and hints
        start_time = time.time()
        hints_used = 0
        max_hints = 3
        
        while True:
            # Show hint option if enabled
            if self.hints_enabled and hints_used < max_hints:
                hint_prompt = f"\nEnter your answer, 'hint' for hint ({max_hints - hints_used} left), or 'skip' to pass: "
            else:
                hint_prompt = f"\nEnter your answer or 'skip' to pass: "
            
            answer = input(hint_prompt).strip().upper()
            
            if answer == "SKIP":
                print(f"Skipped! The word was: {word}")
                return 0, False
            
            elif answer == "HINT" and self.hints_enabled and hints_used < max_hints:
                hints_used += 1
                hint = self.get_hint(word, hints_used)
                print(hint)
                continue
            
            elif answer == word:
                time_taken = time.time() - start_time
                score = self.calculate_score(len(word), time_taken, hints_used)
                
                print(f"\n🎉 CORRECT! Well done, {player_name}!")
                print(f"Word: {word}")
                print(f"Time taken: {time_taken:.1f} seconds")
                print(f"Hints used: {hints_used}")
                print(f"Score earned: {score}")
                
                return score, True
            
            else:
                print("❌ Incorrect. Try again!")
    
    def play_game(self) -> None:
        """Main game loop for two players."""
        print("\n" + "="*60)
        print("🎮 WELCOME TO JUMBLED WORDS GAME! 🎮")
        print("="*60)
        print("A fun word puzzle game for two players!")
        print("\nGame Rules:")
        print("- Players take turns unscrambling jumbled words")
        print("- Correct answers earn points based on word length and speed")
        print("- Hints are available but reduce your score")
        print("- First player to reach 50 points wins!")
        
        # Get player names
        p1_name = input("\nPlayer 1, please enter your name: ").strip()
        p2_name = input("Player 2, please enter your name: ").strip()
        
        # Select category
        self.current_category = self.select_category()
        
        # Game settings
        print(f"\nGame Settings:")
        print(f"Category: {self.current_category}")
        print(f"Hints enabled: {'Yes' if self.hints_enabled else 'No'}")
        
        # Initialize scores
        p1_score = 0
        p2_score = 0
        round_number = 1
        winning_score = 50
        
        # Main game loop
        while p1_score < winning_score and p2_score < winning_score:
            print(f"\n{'='*60}")
            print(f"ROUND {round_number}")
            print(f"Scores: {p1_name}: {p1_score} | {p2_name}: {p2_score}")
            print(f"{'='*60}")
            
            # Player 1's turn
            score1, correct1 = self.play_round(p1_name)
            p1_score += score1
            
            # Check if player 1 won
            if p1_score >= winning_score:
                break
            
            # Player 2's turn
            score2, correct2 = self.play_round(p2_name)
            p2_score += score2
            
            round_number += 1
            
            # Ask if players want to continue
            if round_number <= 5:  # Auto-continue for first 5 rounds
                continue
            
            continue_game = input("\nContinue playing? (y/n): ").lower()
            if continue_game != 'y':
                break
        
        # Game over
        self.display_final_results(p1_name, p1_score, p2_name, p2_score)
    
    def display_final_results(self, p1_name: str, p1_score: int, p2_name: str, p2_score: int) -> None:
        """
        Display the final game results.
        
        Args:
            p1_name (str): Player 1 name
            p1_score (int): Player 1 score
            p2_name (str): Player 2 name
            p2_score (int): Player 2 score
        """
        print("\n" + "="*60)
        print("🏆 GAME OVER! 🏆")
        print("="*60)
        print(f"Final Scores:")
        print(f"{p1_name}: {p1_score} points")
        print(f"{p2_name}: {p2_score} points")
        print("-"*60)
        
        if p1_score > p2_score:
            print(f"🎉 Congratulations {p1_name}! You WIN! 🎉")
        elif p2_score > p1_score:
            print(f"🎉 Congratulations {p2_name}! You WIN! 🎉")
        else:
            print("🤝 It's a TIE! Well played both! 🤝")
        
        print("="*60)
        print("Thank you for playing Jumbled Words!")
    
    def practice_mode(self) -> None:
        """Single player practice mode."""
        print("\n" + "="*60)
        print("📚 PRACTICE MODE")
        print("="*60)
        print("Practice your word unscrambling skills!")
        
        self.current_category = self.select_category()
        
        while True:
            score, correct = self.play_round("Player")
            
            continue_practice = input("\nPractice another word? (y/n): ").lower()
            if continue_practice != 'y':
                break
        
        print("Practice session completed. Keep practicing to improve!")

def main():
    """Main function to run the Jumbled Words game."""
    game = JumbledWordsGame()
    
    while True:
        print("\n" + "="*60)
        print("🎮 JUMBLED WORDS GAME MENU")
        print("="*60)
        print("1. Two Player Game")
        print("2. Practice Mode")
        print("3. View Categories")
        print("4. Quit")
        print("="*60)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            game.play_game()
        elif choice == "2":
            game.practice_mode()
        elif choice == "3":
            game.display_categories()
        elif choice == "4":
            print("Thanks for playing Jumbled Words! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
