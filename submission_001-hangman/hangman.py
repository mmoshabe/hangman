#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    
    #TODO: Step 1 - open file and read lines as words
    file_name = open(file_name, 'r')
    words = file_name.readlines()
    file_name.close
    return words

def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """##
    rand_word = random.randint(0, len(words)-1)
    word = words[rand_word]

    rand_char = random.randint(0, len(word)-2 )
    letter = word[rand_char]
    displaying = word.replace(word[rand_char], "_", 1)

    print('Guess the word: '+displaying)

    ##
    return word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    question = input("Guess the missing letter: ")
    answer = question
    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

