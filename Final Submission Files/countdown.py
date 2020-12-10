import random


def countdown_welcome():
    print('''                               
 \ \        / / | |                          
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  ''')

    print('''             
 |__   __|   
    | | ___  
    | |/ _ \ 
    | | (_) |
    |_|\___/  ''')

    print('''                         
  / ____|                | |    | |                    
 | |     ___  _   _ _ __ | |_ __| | _____      ___ __  
 | |    / _ \| | | | '_ \| __/ _` |/ _ \ \ /\ / / '_ \ 
 | |___| (_) | |_| | | | | || (_| | (_) \ V  V /| | | |
  \_____\___/ \__,_|_| |_|\__\__,_|\___/ \_/\_/ |_| |_| ''')

    print()
    print()
    print()

    
def select_characters():
    '''Chooses a random vowel or consonant based on user input '''
    # List that the characters randomly chosen will be appended to
    user_letter = []
    # Vowel List Formation
    # Based on accurate probability distribution
    vowel_list = []
    for count in range(0, 15):
        vowel_list.append("a")
    for count in range(0, 21):
        vowel_list.append("e")
    for count in range(0, 13):
        vowel_list.append("i")
        vowel_list.append("o")
    for count in range(0, 5):
        vowel_list.append("u")

    # Consonant List Formation
    # Based on accurate probability distribution
    consonant_list = []
    for count in range(0, 2):
        consonant_list.append("b")
        consonant_list.append("f")
        consonant_list.append("h")
    for count in range(0, 3):
        consonant_list.append("c")
        consonant_list.append("g")
    for count in range(0, 6):
        consonant_list.append("d")
    for count in range(0, 1):
        consonant_list.append("j")
        consonant_list.append("k")
        consonant_list.append("q")
        consonant_list.append("v")
        consonant_list.append("w")
        consonant_list.append("x")
        consonant_list.append("y")
        consonant_list.append("z")
    for count in range(0, 5):
        consonant_list.append("l")
    for count in range(0, 4):
        consonant_list.append("m")
        consonant_list.append("p")
    for count in range(0, 8):
        consonant_list.append("n")
    for count in range(0, 9):
        consonant_list.append("r")
        consonant_list.append("s")
        consonant_list.append("t")

    user_letter_length = 0
    while user_letter_length != 9:
        # Asks the user for a character
        print("Enter a 'c' or 'C' for a consonant",
              "or a 'v' or 'V' for a vowel: ")
        letter_choice = input()
        if letter_choice.lower() == "c":
            cons_num = random.randint(0, 73)
            user_consonant = consonant_list[cons_num]
            print("The letter you got was: ", user_consonant)
            user_letter.append(user_consonant)
            user_letter_length = user_letter_length + 1
        elif letter_choice.lower() == "v":
            vowel_num = random.randint(0, 66)
            user_vowel = vowel_list[vowel_num]
            print("The letter you got was: ", user_vowel)
            user_letter.append(user_vowel)
            user_letter_length = user_letter_length + 1
        else:
            print("Error: you can only enter the following characters",
                  " c, C, v, V")
            print("Please Try Again: ")

    for list_element in user_letter:
        print(list_element, end="")
        
    return user_letter 


def dictionary_reader(testing = False):
    ''' Reads the text file and appends each word to a list '''
    # List that words from the text file will be added
    word_list = []
    user_file = open("words.txt", "r")
    for file_line in user_file:
        accepted_line = file_line.split()
        # Adds each word in the file to a list
        if len(accepted_line[0]) > 9:
            pass
        else:
            word_list.append(accepted_line[0])
    user_file.close()
    return word_list


def word_lookup(dictionary_reader, select_characters):
    ''' Evaluates user's guess and generates longest possible word '''
    user_word = ""
    dictionary_list = dictionary_reader()
    user_letter_list = select_characters()
    
    # Check Word is Acceptable
    print()
    entered_word = None
    valid_word = None
    while entered_word != True:
        # This is the amount of letters that have been
        # checked within the word entered by the user
        checked_letters = 0
        print("Enter the longest word you possibly can from",
              "the group of random characters: ")
        user_word = input()
        # This accomodates the fact that the user,
        # might have entered a word that is not in the dictionary
        if user_word not in dictionary_list:
            print("Error: Word Not in Dictionary")
            print("You have scored 0 points")
            entered_word = True
        else:
            # Each letter in word entered by user
            # is placed into an element in the list
            user_word_list = list(user_word)
            for list_index in user_word_list:
                # Covers that the user might have entered a letter in their word
                # that is not in the group of letters randomly generated earlier
                if list_index not in user_letter_list:
                    print("Error: Invalid Character In Word")
                    print("You have scored 0 points")
                    entered_word = True
                    break
                else:
                    checked_letters = checked_letters + 1
            if checked_letters == len(user_word_list):
                # This is the amount of letters that have been checked
                passed_letters = 0
                for letter_to_analyse in user_word_list:
                    # Letter being currently searched for throughout the word
                    user_token = 0
                    # Variable increments everytime the 'letter_to_analyse'
                    # is found in the group of randomly chosen characters
                    random_token_count = 0
                    for list_aspect in user_word_list:
                        # Compare the character being checked to letter_to_analyse
                        if list_aspect == letter_to_analyse:
                            # If letter_to_analyse and the character being checked are the same:
                            # The varaible increments
                            user_token = user_token + 1
                    for list_piece in user_letter_list:
                        # Checks if the character being checked
                        # is the same as the letter_to_analyse
                        if list_piece == letter_to_analyse:
                            random_token_count = random_token_count + 1
                    # The amount of times 'letter_to_analyse' is found in user_word_list
                    # and user_letter_list is compared
                    if user_token <= random_token_count:
                        passed_letters = passed_letters = passed_letters + 1
                if passed_letters == len(user_word_list):
                    entered_word = True
                    valid_word = True
                else:
                    print("Error: You have entered a letter from the",
                          "random character list too many times")
                    print("You have scored 0 points")
                    entered_word = True

    if valid_word == True:
        # Statement displayed if user has entered valid statement
        print("Valid Word Entered")
        user_score = len(user_word_list)
        print("You have scored", user_score, "points")

    # Computer Finding Best Possible Word
    print("Here are all the longest possible words",
          "you could have possibly got: ")
    # List of ,all the possible words made from the list of random characters
    valid_word_list = []
    # Checks every word from the text file that has been added to the list
    for word_to_analyse in dictionary_list:
        valid_letters = 0
        # List of characters from word
        # That are currently being analysed
        analyse_list = list(word_to_analyse)
        for list_number in analyse_list:
            if list_number not in user_letter_list:
                break
            else:
                valid_letters = valid_letters + 1
        if valid_letters == len(analyse_list):
            valid_word_list.append(word_to_analyse)

    increased_valid_list = []
    # Loops through all the valid words
    for list_part in valid_word_list:
        # Counts the amount of accepted characters
        passed_characters = 0
        # Word being inspected is split into a list
        inspect_list = list(list_part)
        # Loops through the characters in the word being inspected
        for current_letter in inspect_list:
            dictionary_token = 0
            random_token = 0
            for list_item in inspect_list:
                if list_item == current_letter:
                    dictionary_token = dictionary_token + 1
            for list_detail in user_letter_list:
                if list_detail == current_letter:
                    random_token = random_token + 1
            if dictionary_token <= random_token:
                passed_characters = passed_characters + 1
        if passed_characters == len(inspect_list):
            increased_valid_list.append(list_part)
           
    sorted_words_list = sorted(increased_valid_list, key=len)
    longest_word_location = (len(sorted_words_list)) - 1
    longest_word_length = len(sorted_words_list[longest_word_location])
    for list_location in range(((len(sorted_words_list)-1)), 0, -1):
        if len(sorted_words_list[list_location]) == longest_word_length:
            print()
            print(sorted_words_list[list_location])
            print()
            

def testing_framework():
    user_file = open("words.txt", "r")
    # Dictionary Reader Testing
    word_list = []
    for file_line in user_file:
        accepted_line = file_line.split()
        # Adds each word in the file to a list
        if len(accepted_line[0]) > 9:
            pass
        else:
            word_list.append(accepted_line[0])
    user_file.close()
   
    if dictionary_reader(testing = True) == word_list:
        print(" Dictionary Reader Test Passed")
    else:
        print("Dictionary Reader Test Failed")


def main():
    ''' Independent Module  '''
    countdown_welcome()
    testing_framework()
    word_lookup(dictionary_reader, select_characters)

if __name__ == "__main__":
    main()
