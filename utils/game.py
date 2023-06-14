import random #import random lib voor een wilkeurig woord te kiezen

class Hangman:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematic', 'sessions']
        self.word_to_find = random.choice(self.possible_words)
        self.lives = 5
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
    #Class hangman constructor


    def play(self):
        guessed_word = ' '.join([letter if letter in self.correctly_guessed_letters else '_' for letter in self.word_to_find])
        print(f"Word:", guessed_word)
        print(f"Lives: {self.lives}")

        guess = input("Enter a letter: ").lower()
        self.turn_count += 1

        if guess.isalpha() and len(guess) == 1:
            if guess in self.word_to_find:
                self.correctly_guessed_letters.append(guess)
            else:
                self.wrongly_guessed_letters.append(guess)
                self.error_count += 1
                self.lives -= 1
        else:
            print("Enter a single letter")
    """
    in the start we use comprehensions to iterate over evry letter and checks if it is in correctly guessed else it will print _
    asking for a input putting it automaticly in lower case cause it didn't work when i tried uppercase
    checking if the guess is in the alphabet and the length of the guess is 1
    if the guess is correct the guessed letter will be added to correctly guessed_letters else it will add it to wrongly and add error counter +1 and lives -1
    """ 

    def start_game(self):
        while True:
            self.play()
            if self.lives == 0:
                self.game_over()
                break
            elif set(self.word_to_find) == set(self.correctly_guessed_letters):
                self.well_played()
                break
    #Keep playing untill lives are 0 or you guessed the word right 
    def game_over(self):
        print("GAME OVER")
        print(f"The word was: {self.word_to_find}")
    
    #Message if you fail the game

    def well_played(self):
        print(f"You found {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors.")

    #Play this message when you guessed the word right