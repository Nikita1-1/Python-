





def start(nice = 0, mean = 0, name = ''):
   name = describe_game(name)
   nice, mean, name = nice_mean(nice,mean,name)




def describe_game(name):
    """ check if this is a new game or not,
        if it is  new, get the user`s name,
        if it is not a new game, thnk the player for
        playing again and continue wiht the game
    """
    
    if name != "":
        print('\nthank you for playing again, {}'.format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input('\nWhat is your name?>>>').capitalize()
                if name != "":
                    print('Welcome, {}'.format(name))       
                    print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                    print('but at the end of the game your fate will be sealed by your actions')
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input('\nAstranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M)\n>>> ').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)

def show_score(nice, mean, name):
    print('\n{}, your current total is: \n({},Nice) and ({}, Mean)'.format(name,nice,mean))



def score(nice, mean, name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2:#if condition is tru then call win function
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print('\nNice Job {}, you win! \nEveryone loves you and you have made lots of friends along the way!'.format(name))
    again(nice, mean, name)


def lose(nice, mean, name):
    print('\nAaah too bad, gave over: \n{} you live in dirty beat-up van by the river, wretched and alone'.format(name))
    again(nice,mean,name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? Y/N:>>> ').lower()
        if choice == 'y':
            stop = False
            reset(nice, mean, name)
        if choice == 'n':
            print('\nOh, so bad, sorry to see you go')
            stop = False
            quit()
        else:
            print('\nEnter { Y } for "YES", { N } for "NO":\n>>>')


def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)




if __name__ == '__main__':
    start()
