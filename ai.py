"""
Jaden Russell
4/20/2026

This file defines the AI class that records the player's moves in a frequency table, predicts the next move the player will make
based on the sequences in the frequency table, picks the optimal move using the inverse of the BEATS dictionary, and calculates probabilities 
of each move the player will play to display the AI thinking.
"""

import random

MOVES = ['R', 'P', 'S']

# Corresponding move that beats a defined move.
BEATS = {
    'R': 'S',
    'P': 'R',
    'S': 'P',
}

# Creates a dict to hold the optimal move against a defined move (Inverse of BEATS).
COUNTER = {v: k for k, v in BEATS.items()}


class AI:
  
  # Defines the window size of past moves and frequency table to map patterns of past move counts.
    def __init__(self, window_size=2):
        self.window_size = window_size
        self.freq_table = {}

  # Adds the recent player's move to freq_table to record the sequence. Returns if there is not enough moves to learn from.
    def record(self, history, player_move):

      # Not enough move history yet.
        if len(history) < self.window_size:
            return

      # Adds new sequence to the freq_table and/or adds to an existing sequence's count number.
        key = self._make_key(history)
        if key not in self.freq_table:
            self.freq_table[key] = {'R': 0, 'P': 0, 'S': 0}

        self.freq_table[key][player_move] += 1


  # Checks the move window for a sequence and returns the move the player will most likely make based on the pattern.
    def predict(self, history):
      
      # returns random move if not enough moves to learn from.
        if len(history) < self.window_size:
            return random.choice(MOVES)

      # Checks the table for a pattern and defines total number of times it appears.
        key = self._make_key(history)
        counts = self.freq_table.get(key, {})
        total = sum(counts.values())
      
      # returns random move if sequence was not encountered before
        if total == 0:
            return random.choice(MOVES)

        # Return the move the player has played most after this sequence.
        return max(counts, key=counts.get)
      

  # Returns the optimal move after predicting the player's move.
    def pick_move(self, history):
        predicted = self.predict(history)
        return COUNTER[predicted]


  # Return the probability (0–100) for each of the player's moves.
    def get_probabilities(self, history):

      # default probability is 33% for each move.
        default = {'R': 33, 'P': 33, 'S': 34}

        if len(history) < self.window_size:
            return default

      # Checks the table for a pattern and defines total number of times it appears.
        key = self._make_key(history)
        counts = self.freq_table.get(key, {})
        total = sum(counts.values())

      # Return default probability if pattern wasn't encountered
        if total == 0:
            return default

      # return the probability of each move ()
        return {
          # Probability is the number of times a specific move appears in a sequence divided by the total times a sequence appears times 100
            move: round(count / total * 100)
            for move, count in counts.items()
        }

  # Turn the last N (window size) moves into a string key, e.g. ['R','P'] → 'RP'.
    def _make_key(self, history):
        return ''.join(history[-self.window_size:])
