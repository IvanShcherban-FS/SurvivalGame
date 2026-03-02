import random

start_hp = 100
max_turn = 10
enemy_dm = 30
trap_dm = 15
heal_amount = 20
coin = 10
bar_len = 20
goal_coins = 100
greedy_turns = 12

TEXT = {
    "en": {

        "menu_title": "=== Survival Game ===",
        "start": "1. Start Game",
        "results": "2. Results",
        "exit": "3. Exit",
        "enter_mode": "Enter mode: ",
        "invalid_option": "Invalid option!",


        "enter_name": "Enter your name: ",
        "choose_mode": "Choose Mode:",
        "mode_selected": "Mode selected:",
        "enter_mode_1_5": "Enter mode (1-5): ",

        "m_classic": "1. Classic",
        "m_endless": "2. Endless",
        "m_greedy": "3. Greedy",
        "m_hardcore": "4. Hardcore",
        "m_chaos": "5. Chaos",


        "welcome": "\nWelcome to Survival Game",
        "started": "Game started!",


        "goal": "Goal: {goal} coins in {turns} turns",
        "rests_left": "Rests left: {n}",
        "turn": "Turn:",
        "hp": "HP:",
        "coins": "Coins:",


        "choose_action": "\nChoose action:",
        "explore": "1. Explore",
        "rest": "2. Rest",
        "risk": "3. Risk",
        "enter_choice": "Enter your choice: ",


        "enemy": "\nEnemy attacked! You lost {dmg} HP",
        "treasure": "\nYou found treasure! You get {coins} coins",
        "trap": "\nTrap! You lost {dmg} HP",
        "big_treasure": "\nYou found BIG treasure! You get {coins} coins",

        "heal": "\nYou healed {hp} HP",
        "hp_full": "\nYour HP is full. Rest isn't needed",


        "hc_block": "\nHardcore: You already used Rest!",


        "chaos_dd": "CHAOS: Double Damage!",
        "chaos_dc": "CHAOS: Double Coins!",
        "chaos_heal": "CHAOS: Bonus Heal +10 HP!",
        "chaos_none": "CHAOS: Nothing happened!",


        "lose": "You lose! Your HP = 0",
        "win": "You win!",
        "greedy_win": "You win! Coin goal reached!",
        "greedy_lose": "You lose! Didn't reach coin goal",


        "no_scores": "No scores saved",
        "stopped": "Game stopped, Bye!"
    },

    "ua": {

        "menu_title": "=== Гра Виживання ===",
        "start": "1. Почати гру",
        "results": "2. Результати",
        "exit": "3. Вийти",
        "enter_mode": "Виберіть пункт: ",
        "invalid_option": "Невірний варіант!",


        "enter_name": "Введіть ім'я: ",
        "choose_mode": "Оберіть режим:",
        "mode_selected": "Обрано режим:",
        "enter_mode_1_5": "Введіть режим (1-5): ",

        "m_classic": "1. Класичний",
        "m_endless": "2. Нескінченний",
        "m_greedy": "3. Жадібний",
        "m_hardcore": "4. Хардкор",
        "m_chaos": "5. Хаос",


        "welcome": "\nЛаскаво просимо до гри Виживання",
        "started": "Гру розпочато!",


        "goal": "Ціль: {goal} монет за {turns} ходів",
        "rests_left": "Відпочинків залишилось: {n}",
        "turn": "Хід:",
        "hp": "HP:",
        "coins": "Монети:",


        "choose_action": "\nОберіть дію:",
        "explore": "1. Дослідити",
        "rest": "2. Відпочити",
        "risk": "3. Ризик",
        "enter_choice": "Ваш вибір: ",


        "enemy": "\nВорог атакував! Ви втратили {dmg} HP",
        "treasure": "\nЗнайдено скарб! +{coins} монет",
        "trap": "\nПастка! Ви втратили {dmg} HP",
        "big_treasure": "\nВеликий скарб! +{coins} монет",

        "heal": "\nВи відновили {hp} HP",
        "hp_full": "\nHP повне. Відпочинок не потрібен",


        "hc_block": "\nHardcore: відпочинок вже використано!",


        "chaos_dd": "ХАОС: Подвійний урон!",
        "chaos_dc": "ХАОС: Подвійні монети!",
        "chaos_heal": "ХАОС: Бонус +10 HP!",
        "chaos_none": "ХАОС: Нічого не сталося!",


        "lose": "Ви програли! HP = 0",
        "win": "Ви перемогли!",
        "greedy_win": "Перемога! Ціль монет досягнута!",
        "greedy_lose": "Поразка! Ціль не досягнута",


        "no_scores": "Результатів немає",
        "stopped": "Гру завершено!"
    }
}

def t(lang, key):
    return TEXT[lang][key]

def show_menu(lang):
    while True:
        print("\n" + t(lang, "menu_title"))
        print(t(lang, "start"))
        print(t(lang, "results"))
        print(t(lang, "exit"))

        choice = input(t(lang, "enter_mode"))
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print(t(lang, "invalid_option"))


def start_game(lang):
    name = input(t(lang, "enter_name"))

    print("\n" + t(lang, "choose_mode"))
    print(t(lang, "m_classic"))
    print(t(lang, "m_endless"))
    print(t(lang, "m_greedy"))
    print(t(lang, "m_hardcore"))
    print(t(lang, "m_chaos"))

    while True:
        game_mode = input(t(lang, "enter_mode_1_5"))
        if game_mode in ["1", "2", "3", "4", "5"]:
            break
        else:
            print(t(lang, "invalid_option"))

    print(t(lang, "mode_selected"), game_mode)

    hp = start_hp
    coins = 0
    turn = 1
    rests_left = 1

    print(t(lang, "welcome"))
    print(t(lang, "started"))

    while True:

        if game_mode == "3":
            print(t(lang, "goal").format(goal=goal_coins, turns=greedy_turns))

        if game_mode == "4":
            print(t(lang, "rests_left").format(n=rests_left))

        dmg_mult = 1
        coin_mult = 1

        if game_mode == "5":
            r = random.randint(1, 4)
            if r == 1:
                dmg_mult = 2
                print(t(lang, "chaos_dd"))
            elif r == 2:
                coin_mult = 2
                print(t(lang, "chaos_dc"))
            elif r == 3:
                hp += 10
                if hp > start_hp:
                    hp = start_hp
                print(t(lang, "chaos_heal"))
            else:
                print(t(lang, "chaos_none"))

        choice = player_choice(lang)

        if game_mode == "4" and choice == 2 and rests_left == 0:
            print(t(lang, "hc_block"))
            continue

        hp, coins, used_turn = make_event(choice, hp, coins, dmg_mult, coin_mult, lang)

        if game_mode == "4" and choice == 2 and used_turn:
            rests_left -= 1

        if used_turn:
            print_status(turn, hp, coins, lang)

            if hp <= 0:
                print(t(lang, "lose"))
                save_score(name, turn, coins)
                break

            if game_mode == "1" and turn >= max_turn:
                print(t(lang, "win"))
                save_score(name, turn, coins)
                break

            if game_mode == "3":
                if coins >= goal_coins:
                    print(t(lang, "greedy_win"))
                    save_score(name, turn, coins)
                    break
                elif turn >= greedy_turns:
                    print(t(lang, "greedy_lose"))
                    save_score(name, turn, coins)
                    break

            turn += 1


def player_choice(lang):
    while True:
        print(t(lang, "choose_action"))
        print(t(lang, "explore"))
        print(t(lang, "rest"))
        print(t(lang, "risk"))
        choice = input(t(lang, "enter_choice"))

        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print(t(lang, "invalid_option"))


def make_event(choice, hp, coins, dmg_mult, coin_mult):
    event_text = ""
    used_turn = True
    if choice == 1:
        random_num = random.randint(1, 2)
        if random_num == 1:
            damage = enemy_dm * dmg_mult
            hp = hp - damage
            if hp < 0:
                hp = 0
            event_text = f"\nEnemy attacked! You lost {damage} HP"
        else:
            gain = coin * coin_mult
            coins = coins + gain
            event_text = f"\nYou found treasure! You get {gain} coins"

    elif choice == 2:
        if can_rest(hp):
            hp += heal_amount
            if hp > start_hp:
                hp = start_hp
            event_text = f"\nYou healed {heal_amount} HP"
        else:
            used_turn = False
            event_text = ""

    elif choice == 3:
        random_num = random.randint(1, 2)
        if random_num == 1:
            damage = trap_dm * dmg_mult
            hp = hp - damage
            if hp < 0:
                hp = 0
            event_text = f"\nTrap! You lost {damage} HP"
        else:
            gain = (coin*2) * coin_mult
            coins += gain
            event_text = f"\nYou found BIG treasure! You get {gain} coins"
    return hp, coins, event_text, used_turn

def can_rest(hp):
    if hp >= start_hp:
        print("\nYour HP is full. Rest isn't needed")
        return False
    return True

def hp_bar(hp, max_hp):
    filled = int(hp / max_hp * bar_len)
    empty = bar_len - filled
    return "[" + "█" * filled + "░" * empty + "]"

def print_status(turn, hp, coins):
    print(t(lang, "turn"), turn)
    print(t(lang, "hp"), hp_bar(hp), f"{hp}/{start_hp}")
    print(t(lang, "coins"), coins)
    print("------------------")


def game_over(turn, hp, game_mode, coins, goal_coins, greedy_turns):
    is_over = False
    result_text = ""

    if hp <= 0:
        is_over = True
        result_text = "You lose! Your HP = 0"

    elif game_mode == "1":   #Classic
        if turn >= max_turn:
            is_over = True
            result_text = "You win! You survived all turns"

    elif game_mode == "3":   #Greedy
        if coins >= goal_coins:
            is_over = True
            result_text = "You win! You reached the coin goal!!!"
        elif turn >= greedy_turns:
            is_over = True
            result_text = "You lose! You didn't reached the coin goal in time"
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
    print("Choose language / Оберіть мову:")
    print("1. English")
    print("2. Українська")
    l = input("Enter: ")
    if l == "1":
        lang = "en"
        break
    elif l == "2":
        lang = "ua"
        break
    else:
        print("Invalid!")

while True:
    mode = show_menu(lang)
    if mode == 1:
        start_game(lang)
    elif mode == 2:
        show_score(lang)
    elif mode == 3:
        print(t(lang,"stopped"))
        break