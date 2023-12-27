import random

def hangman(word: str)-> None:
    '''
    This function is a simple game of hangman
    '''
    wrong = 0
    stages = ['',
              '_________       ',
              '|        |      ',
              '|        |      ',
              '|        O      ',
              '|       /|\     ',
              '|       / \     ',
              '|               '
              ]
    word = word.lower()
    word_as_list = list(word)
    empty_lines = ['__'] * len(word)
    initial_stage = ['__'] * len(word)
    if ' ' in word_as_list:
        index = word_as_list.index(' ')
        empty_lines[index] = ' '
        initial_stage[index] = ' '          
        
   
    
    initial_stage = ' '.join(initial_stage)    
      
    win = False
    print('\nWelcome to Hangman\n')
    print(initial_stage)
    while wrong < len(stages) - 1 and not win:
        print('\n')
        prompt = ('Guess a letter:\t')
        letter = input(prompt).lower()
        while(len(letter) > 1) :
            letter = input(prompt).lower()
            
        
        my_bool = True
        attempt = 0
        while my_bool: 
            if letter in word_as_list:
                lind = word_as_list.index(letter)
                empty_lines[lind] = letter
                word_as_list[lind] = '$'
                attempt += 1
            elif attempt > 0:
                my_bool = False
            else:
                wrong += 1
                break
            
        result = (' '.join(empty_lines))
        print('\n'.join(stages[:wrong + 1]))
        print('\n' + result)
        if '__' not in empty_lines:
            print('\nYou Win!!!')
            win = True
    if not win:
        print('\nYou lose! It was:', word)



def play_game()-> None:
    lon = ['zebra', 'guitar', 'puzzle', 'picnic', 'cinema', 'monkey', 'flower', 
           'dragon', 'robot', 'cookie', 'pizza', 'ocean', 'rocket', 'unicorn',
           'laptop', 'rainbow', 'cupcake', 'butterfly', 'chocolate', 
           'dinosaur', 'sunshine', 'ice cream', 'hot dog', 'popcorn', 
           'school bus', 'birthday cake', 'tooth fairy', 'roller coaster', 
           'coffee break', 'beach ball', 'fire truck', 'television', 
           'sand castle', 'soccer field', 'rainbow trout', 'bookstore', 
           'mailman', 'ice skates', 'basketball', 'palm tree', 'snow globe']
    
    word = random.choice(lon)
    
    hangman(word)
    
def main() -> None:
    play_game()
    
if __name__ == '__main__':
    main()
    
