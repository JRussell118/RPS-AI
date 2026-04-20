"""
Jaden Russell
4/20/2026

This file defines the functions of the game classs to read and compare the user's input, determine the outcome of the round, 
print the result of the round, and print the scoreboard to show player wins, AI wins and draws.
"""

MOVE_NAMES = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors',
}

# Corresponding move that beats the defined move
BEATS = {
    'R': 'S',
    'P': 'R',
    'S': 'P',
}


class Game:
    def __init__(self):
        self.player_wins = 0
        self.ai_wins     = 0
        self.draws       = 0
        self.rounds      = 0

  # Compare the player and AI's moves and updates the score. Returns the outcome of the player.
    def play_round(self, player_move, ai_move):
        self.rounds += 1
        outcome = self.get_outcome(player_move, ai_move)

        if outcome == 'win':
            self.player_wins += 1
        elif outcome == 'lose':
            self.ai_wins += 1
        else:
            self.draws += 1

        return outcome

  # Returns the round's outcome for the player.
    def get_outcome(self, player, ai):
        if player == ai:
            return 'draw'
        elif BEATS[player] == ai:
            return 'win'
        else:
            return 'lose'

  # Prints a formatted result of the round.
    def print_result(self, player_move, ai_move, outcome):
        p = MOVE_NAMES[player_move]
        a = MOVE_NAMES[ai_move]

        labels = {'win': 'You win!', 'lose': 'AI wins!', 'draw': "It's a draw!"}
        print(f"\nYou: {p}  |  AI: {a}  →  {labels[outcome]}")

  # Prints the overall scores of the AI and player.
    def print_scoreboard(self):
        """Print the running scoreboard."""
        print(f"\n--- Score after {self.rounds} rounds ---")
        print(f"  You: {self.player_wins}  |  AI: {self.ai_wins}  |  Draws: {self.draws}")
