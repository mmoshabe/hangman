import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_index = random.randint(0, len(word)-1)
    new_word = []
    word = 'fool'
    print(word)
    print(random_index)
    for i in range(len(word)):
        if random_index == i:
            new_word.insert(i, word[random_index])
            print(word[random_index], end = '')
        else:
            new_word.insert(i, '_')
            print('_', end = '')
    print()
    new_word = "".join(new_word)
    return new_word   


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    for i in range(0, len(original_word)):
        if (char == original_word[i]) and (answer_word[i] == '_'):
            return True
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    
    for i in range(len(original_word)):
        if char == original_word[i] and answer_word[i] == '_':
            #answer_word[i].replace('_', char, 1)
            answer_word = answer_word[:i] + char + answer_word[i+1:]
            #s = s[:index] + newstring + s[index + 1:]
            break
    #answer_word = "".join(answer_word)    
    return answer_word   



def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    line1 = '/----'
    line2 = '\n|   0'
    line3 = '\n|  /|\\'
    line4 = '\n|   |'
    line5 = '\n|  / \\'
    line6 = '\n_______'
    #print('/----\n' + '|   0\n' + '|\n' * 3) if number_guesses = 4
    if number_guesses == 4:
        print(line1 + '\n|' * 4 + line6)
    elif number_guesses == 3:
        print(line1 + line2 + '\n|' * 3 + line6) 
    elif number_guesses == 2:
        print(line1 + line2 + line3 + '\n|' * 2 + line6) 
    elif number_guesses == 1:
        print(line1 + line2 + line3 + line4 + '\n|' + line6) 
    elif number_guesses == 0:
        print(line1 + line2 + line3 + line4 + line5 + line6) 
    

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    number_guesses = 5
    while number_guesses > 0:
        if answer == word:
            break
        guess = get_user_input()
             
        if guess == 'quit' or guess == 'exit':
            print("Bye!")
            break
    
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:         
            number_guesses = number_guesses-1
            do_wrong_answer(answer, number_guesses)
        if number_guesses == 0:
            print("Sorry, you are out of guesses. The word was: " +word)
            break
        

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

