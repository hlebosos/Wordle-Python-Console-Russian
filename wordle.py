from colorama import Fore, Back, Style
import random
import os
import sys
import time
from colorama import init
init()


alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def clear_screen():
    # Очистка экрана
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor(x, y):
    # ANSI escape последовательность для перемещения курсора
    sys.stdout.write(f"\033[{y};{x}H")


def russianWord(text):
    for letter in text:
        if letter.lower() not in alphabet:
            break
        else:
            continue
        break
    else:
        return True
    return False


script_dir = os.path.dirname(__file__)
word5_file_path = os.path.join(script_dir, 'word5.txt')


num_word = -1
hidden_word = []
word = ""


def randomWord():
    with open(word5_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    file.close()
    num_word = random.randint(1, len(lines))
    return list(lines[num_word].upper()), num_word


def Game():
    hidden_word, num_word = randomWord()
    print(Style.BRIGHT+Fore.CYAN+"Слово загадано, У тебя 6 попыток")
    print("Введите слова: " + Style.RESET_ALL)
    used_leters = {_.upper(): 0 for _ in alphabet}
    posX, posY = 0, 3
    for i in range(6):

        word_is_true = False

        while not word_is_true:
            move_cursor(posX, posY)

            word = input().upper()
            if russianWord(word) and len(word) == 5:
                word_is_true = True
            else:
                move_cursor(posX, posY)

                for _ in "Введите слово из 5 букв русского алфавита!":
                    print(Style.DIM+Fore.RED+_, end="", flush=True)
                    time.sleep(0.03)
                time.sleep(0.5)
                move_cursor(posX, posY)
                print(Style.RESET_ALL+" "*50)
                move_cursor(posX, posY)

        word = list(word)
        move_cursor(posX, posY)
        if word+["\n"] == hidden_word:
            for h in word:
                print(Style.BRIGHT + Back.GREEN +
                      h + Style.RESET_ALL, end=" ", flush=True)
                time.sleep(0.2)

            for _ in f"Ты угадал! Молодец!\n{("('・ω・')", "(/◕ヮ◕)/", "ᶘᵒᴥᵒᶅ", "( ͡° ͜ʖ ͡°)")[random.randint(0, 3)]}\n":
                print(Fore.MAGENTA+_+Style.RESET_ALL, end="", flush=True)
                time.sleep(0.08)

            break

        for l in range(len(word)):

            if word[l] in hidden_word:
                if word[l] == hidden_word[l]:
                    print(Style.BRIGHT + Back.GREEN +
                          word[l] + Style.RESET_ALL, end=" ", flush=True)
                    if word[l] in used_leters:
                        used_leters[word[l]] = 1
                else:
                    print(Style.BRIGHT + Back.YELLOW +
                          word[l] + Style.RESET_ALL, end=" ", flush=True)
                    if word[l] in used_leters and used_leters[word[l]] != 1:
                        used_leters[word[l]] = 2
            else:
                print(Back.LIGHTBLACK_EX +
                      word[l] + Style.RESET_ALL, end=" ", flush=True)
                if word[l] in used_leters:
                    used_leters[word[l]] = 3

            time.sleep(0.1)

        # print(used_leters)

        p1, p2 = 0, 0

        for k, v in used_leters.items():

            move_cursor(60+p1, 5+p2)
            print((Back.BLACK + Style.RESET_ALL, Style.BRIGHT + Back.GREEN, Style.BRIGHT + Back.YELLOW,
                  Back.BLACK + Fore.LIGHTRED_EX)[v]+str(k) + Style.RESET_ALL, end="")
            p1 += 3
            if (p1+15) % 20 == 0:
                p1 = 0
                p2 += 1
        else:
            p1 = 0
            p2 = 0

        posY += 2
        move_cursor(0, posY)
    else:
        for _ in f"К сожилению ты проиграл... {("ಠ_ಠ", "ಠxಠ", "(⚆_⚆)", "☹", "(-ㅅ-)", "(・へ・)", "(´-﹏-`；)")[random.randint(0, 6)]}\nПовезёт в следующий раз!":
            print(Fore.MAGENTA+_+Style.RESET_ALL, end="", flush=True)
            time.sleep(0.05)
        print("")
        print(Fore.YELLOW+Back.BLACK +
              f"Загаданое слово - {"".join(hidden_word)}"+Fore.BLACK+f"index={num_word+1}" + Style.RESET_ALL)


def main():

    # Wordle
    print("-----------------"+Fore.BLACK+Back.YELLOW+"W" + Style.RESET_ALL + " "
          + Fore.YELLOW+Back.BLACK+"O" + Style.RESET_ALL + " "
          + Fore.BLACK+Back.YELLOW+"R" + Style.RESET_ALL + " "
          + Fore.YELLOW+Back.BLACK+"D" + Style.RESET_ALL + " "
          + Fore.BLACK+Back.YELLOW+"L" + Style.RESET_ALL + " "
          + Fore.YELLOW+Back.BLACK+"E" + Style.RESET_ALL + " "
          + Style.RESET_ALL+"----------------")

    time.sleep(0.2)

    # logo
    print("                                   ", end="")

    for _ in "by HLeeb_":
        print(Fore.CYAN+_, end="", flush=True)
        time.sleep(0.1)
    else:
        print("\n"+Style.RESET_ALL)
    time.sleep(0.2)

    # rule
    print("Правила очень просты:",
          "•Загадано слово из 5 русских букв.",
          "•Каждым ходом игрок вводит свое слово, а програма определяет какие буквы входят в слово.",
          " " + Style.BRIGHT+Back.GREEN + " " + Style.RESET_ALL +
          " " + "- Буква есть в слове и стоит на своём месте",
          " " + Style.BRIGHT+Back.YELLOW + " " + Style.RESET_ALL +
          " " + "- Буква есть в слове, но она стоит не на своём месте",
          " " + Back.LIGHTBLACK_EX + " " + Style.RESET_ALL +
          " " + "- Буквы нет в загаданом слове", "Удачи!",
          sep="\n")

    for _ in "Enter начать...":
        print(_, end="", flush=True)
        time.sleep(0.04)
    input()
    clear_screen()
    move_cursor(0, 0)
    Game()  # Enter Game
    while input('Enter -> продолжить;\nЛюбая клавиша-> выйти:\n') == "":  # relode
        clear_screen()

        Game()


# print(Fore.GREEN + 'зеленый текст')
# print(Back.YELLOW + 'на желтом фоне')
# print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
# print('обычный текст')
if __name__ == "__main__":
    main()
print(num_word, hidden_word, word)
