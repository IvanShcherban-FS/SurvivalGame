import random

start_hp = 100
max_turn = 10
enemy_dm = 30
trap_dm = 15
heal_amount = 20
coin = 10


def show_menu():
    while True:
        print("===Survival Game===")
        print("1. Start Game")
        print("2. Results")
        print("3. Exit")

        choice = input("Enter Mode: ")
        if choice == "1" or choice == "2" or choice == "3":
            return int(choice)
        else:
            print("Error, Enter a valid option")


def start_game():
    name = input("Enter your name: ")
    hp = start_hp
    coins = 0
    turn = 1
    print("\nWelcome to Survival Game")
    print("Game started!")
    while True:
        print("Your HP:", hp)
        choice = player_choice()
        hp, coins, event_text = make_event(choice, hp, coins)
        print(event_text)
        print_status(turn, hp, coins)
        is_over, result_text = game_over(turn, hp)
        if is_over:
            print(result_text)
            save_score(name, turn, coins)
            break
        turn += 1


def player_choice():
    while True:
        print("\n Choose action:")
        print("1. Explore")
        print("2. Rest")
        print("3. Risk")
        choice = input("Enter your choice: ")
        if choice == "1" or choice == "2" or choice == "3":
            return int(choice)
        else:
            print("Error chose, Try again")


def make_event(choice, hp, coins):
    event_text = ""
    if choice == 1:
        random_num = random.randint(1, 2)
        if random_num == 1:
            hp = hp - enemy_dm
            event_text = f"Enemy attacked! You lost {enemy_dm} HP"
        else:
            coins = coins + coin
            event_text = f"You found treasure! You get {coin} coins"
    elif choice == 2:
        hp = hp + heal_amount
        event_text = f"You healed {heal_amount} HP"
    elif choice == 3:
        random_num = random.randint(1, 2)
        if random_num == 1:
            hp = hp - trap_dm
            event_text = f"Trap! You lost {trap_dm} HP"
        else:
            coins += coin*2
            event_text = f"You found BIG treasure! You get {coin*2} coins"
    return hp,coins, event_text

def print_status(turn, hp, coins):
    print("Turn:", turn)
    print("HP:", hp)
    print("Coins:", coins)
    print("------------------")


def game_over(turn, hp):
    is_over = False
    result_text = ""

    if hp <= 0:
        is_over = True
        result_text = "You lose! Your HP = 0"
    elif turn >= max_turn:
        is_over = True
        result_text = "You win! You survived all turns"
    return is_over, result_text


def save_score(name, turn, coins):
    pass


def load_score():
    pass


def show_score():
    pass



while True:
    mode = show_menu()
    if mode == 1:
        start_game()
    elif mode == 2:
        show_score()
    elif mode == 3:
        print("Game stopped, Bye!")
        break