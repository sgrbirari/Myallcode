def printBoard(xState, zState):
    print(f'0 | 1 | 2 ')
    print(f'--|---|-- ')
    print(f'3 | 4 | 5 ') 
    print(f'--|---|-- ')
    print(f'6 | 7 | 8 ')
    
if __name__== '__main__':
    xState=[0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0]
    turn=1 # 1for X and 0 for O
    
    print('welcome to Tic Tac Toe!!!')
    while(True):
        if (turn== 1):
            print('Xs chance')
            value= int(input('please enter a value'))
            xState[value]=1
        else:
            print('Zs chance')
            value= int(input('please enter a value'))
            zState[value]=1
            printBoard()
            break