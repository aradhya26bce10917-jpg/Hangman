class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 6
        self.score = 0
        self.guessed_letters = []

    def lose_life(self):
        self.lives -= 1

    def add_score(self):
        self.score += 1

    def add_guess(self, letter):
        self.guessed_letters.append(letter)