# RouletteGame Code
import colorama
from colorama import Fore, Back, Style, init
import os
import sys
import time
import random

colorama.init()
os.system("cls" or "clear")

class Game:
    def spinRoulette():
        return random.randint(1, 50)

    def getUserBet():
        while True:
            user_input = input("Place your bet! Type 'odd' or 'even': ").lower()
            if user_input in ['odd', 'even']:
                return user_input
            else:
                print("Invalid input. Please enter 'odd' or 'even'.")
    def play_roulette():
        userBalance = 100 # Starting balance.
        while userBalance > 0:
            print(f"\nYour current balance: {userBalance}")

            # Spin the roulette wheel.
            results = Game.spinRoulette()
            print(f"\nThe roulette wheel spins... and lands on {result}!")
            # Parse the user's bet
            userBet = Game.getUserBet()

            # Check if player wins or loses.
            if (results % 2 == 0 and userBet == 'even') or (results % 2 != 0 and userBet == 'odd'):
                print("Congratulations! You win!")
                userBalance += 10
            else:
                print("Oops, you just drained yoself 10 buckaroonies.")
                userBalance -+ 10
        print("\nGame over. You are out of balance.")



class Welcome:
    def welcomeMessage():
        print("[" + Fore.GREEN + "LOADED" + Fore.WHITE + "] Game loaded. Welcome to RouletteGame!")
        Game.play_roulette()
