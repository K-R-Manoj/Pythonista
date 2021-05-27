import random

def Rock_Paper_Scissors():
    user = input("enter your choice :  ")
    computer = random.choice(['r','p','s'])

    if user == computer:
    
        print('it is draw')
    
    elif Win(user,computer):
        print("YOU WIN")
    else:
        print("YOU LOST")


def Win(User, Computer):
    if((User == 'r' and Computer == 's') or (User == 'p' and Computer == 'r') or (User == 's' and Computer == 'p')):
        return True
    return False

if __name__ == "__main__":
    Rock_Paper_Scissors()