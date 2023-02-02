def g_command(start_word):
    game_command = input(f"{start_word} игру? да/нет: ")
    while True:
        if game_command == "да":
            is_game = True
            break
        elif game_command == "нет":
            is_game = False
            break
        else:
            print("Введена неизвестная комманда")
            game_command = input(f"{start_word} игру? да/нет: ")
    return is_game

def q_num(num, start_word):
    while True:
        quess_num = int(input("Загадано число. Угадайте его: "))
        if quess_num == num:
            print("Ура, ты угадал число!")
            start_word = "Продолжаем"
            break
        elif quess_num < num:
            print("Неверно. Нужно число БОЛЬШЕ")
        elif quess_num > num:
            print("Неверно. Нужно число МЕНЬШЕ")
        else:
            print("Введена неизвестная комманда")
    return start_word