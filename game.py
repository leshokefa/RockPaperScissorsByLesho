from colorama import Fore, Back, Style
import random
running = True
score = 0
while running:
    n = 1
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    player_move = input("Choose your move: [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else: 
        raise SystemExit(Fore.RED + "False input. Please try again..")

    computer_random_move = random.randint(1, 3)
    computer_move = "";
    if computer_random_move == 1:
        computer_move = rock
        print(Fore.BLUE + "The computer chose rock!" + Style.RESET_ALL)
    elif computer_random_move == 2:
        computer_move = paper
        print(Fore.BLUE + "The computer chose paper!" + Style.RESET_ALL)
    else:
        computer_move = scissors
        print(Fore.BLUE + "The computer chose scissors!" + Style.RESET_ALL)

    if(player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
            print(Fore.GREEN + "You won!" + Style.RESET_ALL)
            score += 10
    elif player_move == computer_move:
        print(Fore.BLUE + "You think like a robot? Draw!" + Style.RESET_ALL)
        score += 5
    else: 
        print(Fore.RED + "You lose!" + Style.RESET_ALL)
    print(Fore.YELLOW + f'You now have {score} points!' + Style.RESET_ALL)
    play_again = input("Wanna play again? (y/n) ")
    if play_again == "no" or play_again == "n":
        running = False
