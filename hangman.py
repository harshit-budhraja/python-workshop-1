import random


def get_file_len(fl):
    """
    Returns the number of lines in a given file.
    """
    count = 0
    fl.seek(0)  # Go to the beginning og the file to be safe
    for line in fl:
        count += 1
    fl.seek(0)
    return count


def get_random_word():
    """
    Fetches a random word from the wordlist.
    """
    f = open('wordfile.txt', 'r')
    lines = f.readlines()

    length = get_file_len(f)
    f.close()
    rand = random.randint(0, length)

    word = lines[rand].strip()  # Remove unwanted new line and space characters
    return word


def run(lives=5):
    """
    Runs our Hangman game with given lives.
    """
    word = get_random_word()
    display_word = '*' * len(word)

    while '*' in display_word and lives > 0:
        print("\nCurrent word: " + display_word)
        print(str(lives) + " lives remaining!")

        ch = input("Enter a character: ")

        for x in range(len(word)):
            if ch == word[x]:
                display_word = list(display_word)
                display_word[x] = ch
                display_word = ''.join(display_word)
        lives -= 1

    if display_word == word:
        print("Congratulations! You've won!")
    else:
        print("You've lost! :(")

if __name__ == '__main__':
    print("Welcome to Hangman!")
    print("Choose difficulty level for the game:")
    print("(1) Low difficulty - 10 lives")
    print("(2) Medium difficulty - 5 lives")
    print("(3) High difficulty - 3 lives")
    dif = int(input("Enter difficulty level: "))

    if dif == 1:
        run(10)
    elif dif == 2:
        run(5)
    elif dif == 3:
        run(3)
    else:
        print("Invalid entry.")
        print("Running game with default difficulty of 5.")
        run()

