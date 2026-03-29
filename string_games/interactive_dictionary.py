"""
Interactive Dictionary - Smart Word Lookup with Suggestions

A comprehensive dictionary application that provides word definitions,
handles different cases, and suggests similar words when exact matches
aren't found.

Features:
- Word definitions from JSON database
- Case-insensitive search
- Fuzzy matching for spelling suggestions
- Word history tracking
- Learning mode with quizzes
- Statistics tracking
"""

import json
import random
from typing import List, Dict, Optional, Tuple
from difflib import get_close_matches
import time

class InteractiveDictionary:
    """Main class for the Interactive Dictionary application."""
    
    def __init__(self, data_file: str = "data.json"):
        """
        Initialize the dictionary.
        
        Args:
            data_file (str): Path to the JSON data file
        """
        self.data_file = data_file
        self.data = {}
        self.search_history = []
        self.favorite_words = []
        self.quiz_score = 0
        self.total_quizzes = 0
        self.load_dictionary()
    
    def load_dictionary(self) -> None:
        """Load dictionary data from JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
            print(f"✓ Dictionary loaded successfully with {len(self.data)} words!")
        except FileNotFoundError:
            print(f"⚠ Warning: {self.data_file} not found.")
            print("Creating a sample dictionary for demonstration...")
            self.create_sample_dictionary()
        except json.JSONDecodeError:
            print(f"⚠ Error: Invalid JSON in {self.data_file}")
            self.create_sample_dictionary()
    
    def create_sample_dictionary(self) -> None:
        """Create a sample dictionary for demonstration purposes."""
        self.data = {
            "python": {
                "noun": [
                    "A large non-venomous snake that constricts its prey.",
                    "A high-level programming language."
                ],
                "adjective": ["Relating to or characteristic of python."]
            },
            "computer": {
                "noun": [
                    "An electronic device for storing and processing data.",
                    "A person who computes; a calculator."
                ]
            },
            "algorithm": {
                "noun": [
                    "A process or set of rules to be followed in calculations or other problem-solving operations.",
                    "A step-by-step procedure for solving a problem or accomplishing a task."
                ]
            },
            "data": {
                "noun": [
                    "Facts and statistics collected together for reference or analysis.",
                    "Information processed or stored by a computer."
                ]
            },
            "network": {
                "noun": [
                    "A group or system of interconnected people or things.",
                    "A system of computers and peripherals that are connected."
                ]
            },
            "programming": {
                "noun": [
                    "The process of writing computer programs.",
                    "The action or process of writing computer programs."
                ]
            }
        }
    
    def translate(self, word: str) -> Tuple[bool, str, List[str]]:
        """
        Translate/lookup a word in the dictionary.
        
        Args:
            word (str): Word to lookup
        
        Returns:
            Tuple[bool, str, List[str]]: (found, result/message, suggestions)
        """
        word_lower = word.lower()
        suggestions = []
        
        # Direct match (case-insensitive)
        if word_lower in self.data:
            self.add_to_history(word_lower, True)
            return True, self.format_definitions(self.data[word_lower]), []
        
        # Title case match
        if word.title() in self.data:
            self.add_to_history(word.title(), True)
            return True, self.format_definitions(self.data[word.title()]), []
        
        # Upper case match
        if word.upper() in self.data:
            self.add_to_history(word.upper(), True)
            return True, self.format_definitions(self.data[word.upper()]), []
        
        # Find close matches
        close_matches = get_close_matches(word, list(self.data.keys()), n=3, cutoff=0.6)
        suggestions = close_matches
        
        if close_matches:
            suggestion_text = f"Did you mean {close_matches[0]}? "
            if len(close_matches) > 1:
                suggestion_text += f"Other suggestions: {', '.join(close_matches[1:])}"
            self.add_to_history(word, False)
            return False, suggestion_text, close_matches
        else:
            self.add_to_history(word, False)
            return False, f"The word '{word}' doesn't exist. Please double-check it.", []
    
    def format_definitions(self, definitions: Dict[str, List[str]]) -> str:
        """
        Format word definitions for display.
        
        Args:
            definitions (Dict[str, List[str]]): Word definitions by part of speech
        
        Returns:
            str: Formatted definition string
        """
        result = []
        for part_of_speech, defs in definitions.items():
            result.append(f"\n{part_of_speech.upper()}:")
            for i, definition in enumerate(defs, 1):
                result.append(f"  {i}. {definition}")
        return "\n".join(result)
    
    def add_to_history(self, word: str, found: bool) -> None:
        """
        Add word to search history.
        
        Args:
            word (str): The searched word
            found (bool): Whether the word was found
        """
        self.search_history.append({
            'word': word,
            'found': found,
            'timestamp': time.time()
        })
        
        # Keep only last 50 searches
        if len(self.search_history) > 50:
            self.search_history = self.search_history[-50:]
    
    def interactive_search(self) -> None:
        """Interactive word search with suggestions."""
        print("\n" + "="*60)
        print("🔍 INTERACTIVE DICTIONARY SEARCH")
        print("="*60)
        print("Type 'quit' to exit, 'history' to see search history")
        print("Type 'favorites' to see favorite words")
        print("-"*60)
        
        while True:
            word = input("\nEnter a word to lookup: ").strip()
            
            if word.lower() == 'quit':
                break
            elif word.lower() == 'history':
                self.display_history()
                continue
            elif word.lower() == 'favorites':
                self.display_favorites()
                continue
            elif not word:
                print("Please enter a word.")
                continue
            
            found, result, suggestions = self.translate(word)
            
            if found:
                print(f"\n✅ Found: {word}")
                print(result)
                
                # Ask if user wants to add to favorites
                add_fav = input("\nAdd to favorites? (y/n): ").lower()
                if add_fav == 'y' and word.lower() not in [w.lower() for w in self.favorite_words]:
                    self.favorite_words.append(word)
                    print(f"✓ '{word}' added to favorites!")
            
            else:
                print(f"\n❌ {result}")
                
                if suggestions:
                    choice = input("\nTry the first suggestion? (y/n): ").lower()
                    if choice == 'y':
                        found, result, _ = self.translate(suggestions[0])
                        if found:
                            print(f"\n✅ Found: {suggestions[0]}")
                            print(result)
    
    def display_history(self) -> None:
        """Display search history."""
        print("\n" + "="*60)
        print("📚 SEARCH HISTORY")
        print("="*60)
        
        if not self.search_history:
            print("No search history yet.")
            return
        
        for i, entry in enumerate(reversed(self.search_history[-10:]), 1):
            status = "✅" if entry['found'] else "❌"
            print(f"{i:2d}. {status} {entry['word']}")
        
        print("="*60)
    
    def display_favorites(self) -> None:
        """Display favorite words."""
        print("\n" + "="*60)
        print("⭐ FAVORITE WORDS")
        print("="*60)
        
        if not self.favorite_words:
            print("No favorite words yet.")
            return
        
        for i, word in enumerate(self.favorite_words, 1):
            print(f"{i}. {word}")
        
        print("="*60)
    
    def quiz_mode(self) -> None:
        """Start a quiz mode to test vocabulary."""
        print("\n" + "="*60)
        print("🎯 VOCABULARY QUIZ")
        print("="*60)
        print("Test your vocabulary knowledge!")
        print("You'll be given definitions and need to guess the word.")
        print("-"*60)
        
        if len(self.data) < 2:
            print("Not enough words for a quiz. Need at least 2 words in dictionary.")
            return
        
        score = 0
        total_questions = 5
        words = list(self.data.keys())
        
        for question_num in range(total_questions):
            # Select a random word
            word = random.choice(words)
            definitions = self.data[word]
            
            # Select a random definition
            all_defs = []
            for part_defs in definitions.values():
                all_defs.extend(part_defs)
            
            if not all_defs:
                continue
            
            definition = random.choice(all_defs)
            
            # Create multiple choice options
            options = [word]
            while len(options) < 4:
                option = random.choice(words)
                if option not in options:
                    options.append(option)
            
            random.shuffle(options)
            
            # Display question
            print(f"\nQuestion {question_num + 1}:")
            print(f"Definition: {definition}")
            print("\nOptions:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            # Get answer
            while True:
                try:
                    answer = int(input("\nYour answer (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Check answer
            selected_word = options[answer - 1]
            if selected_word == word:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer was: {word}")
        
        # Display results
        percentage = (score / total_questions) * 100
        print(f"\n{'='*60}")
        print("🎯 QUIZ RESULTS")
        print(f"{'='*60}")
        print(f"Score: {score}/{total_questions} ({percentage:.1f}%)")
        
        if percentage >= 80:
            print("🏆 Excellent work!")
        elif percentage >= 60:
            print("👍 Good job!")
        elif percentage >= 40:
            print("📚 Keep practicing!")
        else:
            print("💪 More practice needed!")
        
        self.quiz_score += score
        self.total_quizzes += 1
    
    def display_statistics(self) -> None:
        """Display dictionary usage statistics."""
        print("\n" + "="*60)
        print("📊 DICTIONARY STATISTICS")
        print("="*60)
        print(f"Total words in dictionary: {len(self.data)}")
        print(f"Words searched: {len(self.search_history)}")
        print(f"Favorite words: {len(self.favorite_words)}")
        
        if self.search_history:
            successful_searches = sum(1 for entry in self.search_history if entry['found'])
            success_rate = (successful_searches / len(self.search_history)) * 100
            print(f"Search success rate: {success_rate:.1f}%")
        
        if self.total_quizzes > 0:
            avg_quiz_score = self.quiz_score / (self.total_quizzes * 5) * 100  # Assuming 5 questions per quiz
            print(f"Quizzes taken: {self.total_quizzes}")
            print(f"Average quiz score: {avg_quiz_score:.1f}%")
        
        print("="*60)
    
    def add_word(self, word: str, definitions: Dict[str, List[str]]) -> None:
        """
        Add a new word to the dictionary.
        
        Args:
            word (str): Word to add
            definitions (Dict[str, List[str]]): Definitions by part of speech
        """
        word_lower = word.lower()
        self.data[word_lower] = definitions
        print(f"✓ Word '{word}' added to dictionary!")
    
    def save_dictionary(self) -> None:
        """Save dictionary to JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=2)
            print(f"✓ Dictionary saved to {self.data_file}")
        except Exception as e:
            print(f"❌ Error saving dictionary: {e}")

def main():
    """Main function to run the Interactive Dictionary."""
    print("📚 Welcome to the Interactive Dictionary! 📚")
    print("A smart dictionary with suggestions and learning features.")
    
    # Initialize dictionary
    dictionary = InteractiveDictionary()
    
    # Main menu
    while True:
        print("\n" + "="*60)
        print("📚 INTERACTIVE DICTIONARY MENU")
        print("="*60)
        print("1. 🔍 Search for a word")
        print("2. 🎯 Vocabulary Quiz")
        print("3. 📚 View Favorites")
        print("4. 📊 View Statistics")
        print("5. 📝 Search History")
        print("6. ➕ Add new word")
        print("7. 💾 Save dictionary")
        print("8. 🚪 Quit")
        print("="*60)
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == "1":
            dictionary.interactive_search()
        elif choice == "2":
            dictionary.quiz_mode()
        elif choice == "3":
            dictionary.display_favorites()
        elif choice == "4":
            dictionary.display_statistics()
        elif choice == "5":
            dictionary.display_history()
        elif choice == "6":
            word = input("Enter the word: ").strip()
            if word:
                print("Enter definitions (format: part_of_speech: definition1; definition2; ...)")
                def_input = input("Definitions: ").strip()
                # Simple parsing - in a real app, this would be more sophisticated
                dictionary.add_word(word, {"noun": [def_input]})
        elif choice == "7":
            dictionary.save_dictionary()
        elif choice == "8":
            print("Thank you for using the Interactive Dictionary! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
