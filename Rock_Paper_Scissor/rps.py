import random

def Rock_Paper_Scissors():
    print(" Rock : r \n Paper : p \n Scissor : s")
    user = input("Enter your choice :  ")
    computer = random.choice(['r','p','s'])

    if user == 'r' or user == 'p' or user == 's':

        if user == computer:
        
            print('It IS DRAW')
        
        elif Win(user,computer):
            print("YOU WIN")
        else:
            print("YOU LOST")
    else:
        print(" ERROR ...!!!! \n Enter Valid Input \n")


def Win(User, Computer):
    if((User == 'r' and Computer == 's') or (User == 'p' and Computer == 'r') or (User == 's' and Computer == 'p')):
        return True
    return False

if __name__ == "__main__":
    Rock_Paper_Scissors()