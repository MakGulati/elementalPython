import numpy as np

debug=input("mode?  ")
if debug==0:
    print("Starting TicTacToe......")
    p1=input("First Player's name? ")
    print(p1)
    p2=input("Second Player's name? ")
    print(p2)
    op1=input("operator for Player 1: X or 0 ")
    print("You chose: "+op1)
    if op1=="X" or "x":
        op2="0"
    else:
        op2="X"
            
        print("operator for Player 2: "+op2)
    
posn_mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
game_mat=np.array([["-","-","-"],["-","-","-"],["-","-","-"]])

print(posn_mat)
print(game_mat)
        
        
    