"""
Jaden Russell
4/20/2026

This file runs the rock, paper, scissors game against the AI. After inputing a few moves, the AI will recognize a pattern in your inputs,
predict your next move and play an optimal move for a win. You can check the AI probabilites by inputing y when asked for predictions.
Enter r, p, or s to input a move and q to quit. 
"""

from ai import AI
from game import Game

# Move size to detect patterns
WINDOW_SIZE = 2   

VALID_INPUTS = {'r': 'R', 'p': 'P', 's': 'S'}


# Ask the player for their move and return 'R', 'P', or 'S'. Repeats if any other input is detected.
def get_player_move():
    while True:
        user_in = input("Your move (r/p/s) or q to quit: ").strip().lower()
        if user_in == 'q':
            return None
        if user_in in VALID_INPUTS:
            return VALID_INPUTS[user_in]
        print("Invalid input. Please enter r, p, s, or q.")
      

# Prints what the AI currently thinks you'll play next and what move it will decide to play accordingly.
def show_ai_thinking(ai, history):

    probs = ai.get_probabilities(history)
    predicted = ai.predict(history)
    counter   = ai.pick_move(history)

    names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    print(f"\n  [AI Predictions]  R:{probs['R']}%  P:{probs['P']}%  S:{probs['S']}%")
    if len(history) >= ai.window_size:
        print(f"  Predicting you'll play {names[predicted]}, AI will play {names[counter]}")


# Starts the game and teaches the AI
def main():
    print("=" * 45)
    print("  Rock Paper Scissors — Pattern AI")
    print(f"  AI window size: {WINDOW_SIZE} move(s)")
    print("  The AI learns your patterns over time.")
    print("=" * 45 + "\n")

    print("Would you like to see the AI's predictions each round? (y/n)")
    show_ai = input().strip().lower() == 'y'

    ai = AI(window_size=WINDOW_SIZE)
    game = Game()
  
    # internal list of all your previous moves
    history = []   

    while True:
        if show_ai:
            show_ai_thinking(ai, history)

        player_move = get_player_move()
        if player_move is None:
            break

        print("\033[H\033[2J", end="")
      
        # AI picks it's move before seeing the user's input.
        ai_move = ai.pick_move(history)

        outcome = game.play_round(player_move, ai_move)
        game.print_result(player_move, ai_move, outcome)

        # Adds your move to the list of previous moves
        ai.record(history, player_move)
        history.append(player_move)

        game.print_scoreboard()

    print("\nThanks for playing!")
    print("\nFinal Scoreboard:")
    game.print_scoreboard()


if __name__ == "__main__":
    main()
