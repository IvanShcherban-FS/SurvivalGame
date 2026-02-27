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
            event_text = f"\nEnemy attacked! You lost {enemy_dm} HP"
        else:
            coins = coins + coin
            event_text = f"\nYou found treasure! You get {coin} coins"
    elif choice == 2:
        if can_rest(hp):
            hp += heal_amount
            hp = min(hp, start_hp)
            event_text = f"\nYou healed {heal_amount} HP"
        else:
            event_text = "\nYou are already at maximum HP. Rest is not needed."
    elif choice == 3:
        random_num = random.randint(1, 2)
        if random_num == 1:
            hp = hp - trap_dm
            event_text = f"\nTrap! You lost {trap_dm} HP"
        else:
            coins += coin*2
            event_text = f"\nYou found BIG treasure! You get {coin*2} coins"
    return hp,coins, event_text

def can_rest(hp):
    if hp >= start_hp:
        return False
    return True

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
    with open("scores.txt", "a") as f:
        f.write(f"{name},{turn},{coins}\n")

def load_score():
    scores = []
    try:
        with open("scores.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(",")
                name = parts[0]
                turn = int(parts[1])
                coins = int(parts[2])
                scores.append((name, turn, coins))
    except FileNotFoundError:
        return []
    return scores

def show_score():
    scores = load_score()
    print("\n=====RESULTS=====")
    if len(scores) == 0:
        print("No scores saved")
    i = 1
    for score in scores:
        name = score[0]
        turn = score[1]
        coins = score[2]
        print(f"{i}. {name} --Turns: {turn}, Coins: {coins}")
        i += 1

while True:
    mode = show_menu()
    if mode == 1:
        start_game()
    elif mode == 2:
        show_score()
    elif mode == 3:
        print("Game stopped, Bye!")
        break