import random

def Rock_Paper_Scissors():
    user = input("enter your choice :  ")
    computer = random.choice(['r','p','s'])

    if user == computer:
    
        print('it is draw')
    
    elif user == 'r':
    
        if computer == 'p':
        
            print('YOU LOST')
        
        else:
        
            print('You Won')
        
    
    elif user == 'p':
    
        if computer == 's':
        
            print('YOU LOST')
        
        else:
        
            print('YOU WIN')
        
    
    else:
    
        if computer == 'r':
        
            print('YOU LOST')
        
        else:
        
            print('YOU WIN')
        
if __name__ == "__main__":
    Rock_Paper_Scissors()