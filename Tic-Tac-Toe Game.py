#Tic-tac-toe game created by Al Tareen

import random
import pprint
import sys
import copy

userName = str(input('Welcome to tic-tac-toe!\n\nPlease state your name to begin:\n'))
retry = ' '

dictionaryStartBoard = {
    'TL': ' ', 'TM': ' ', 'TR': ' ', \
    'ML': ' ', 'MM': ' ', 'MR': ' ', \
    'BL': ' ', 'BM': ' ', 'BR': ' '
    }

dictionaryPlayerMove = {
    'TL': ' ', 'TM': ' ', 'TR': ' ', \
    'ML': ' ', 'MM': ' ', 'MR': ' ', \
    'BL': ' ', 'BM': ' ', 'BR': ' ', \
    'START': ' '
    }

def lineBreak():
    print('')

def checkIfEmpty(dictionary):
    if dictionary:
        return False
    elif dictionary == None:
        return True

def initialPrintBoard(dictionary):
    print(dictionary['TL'] + '|' + dictionary['TM'] + '|' + dictionary['TR']) 
    print('-+-+-')
    print(dictionary['ML'] + '|' + dictionary['MM'] + '|' + dictionary['MR'])
    print('-+-+-')
    print(dictionary['BL'] + '|' + dictionary['BM'] + '|' + dictionary['BR'])

def TicTacToe():

    playerSymbol = random.choice('ox')
    computerSymbol = ' '
    playerMove = ' '
    computerMove = ' '
    turn = ' '

    if playerSymbol == 'x':
        computerSymbol = 'o'
        playerMove='START'
    else:
        computerSymbol = 'x'
        computerMove='START'
        
    print('\nThank you',  userName + ',', 'let\'s begin!')
    lineBreak()

    print('You have randomly been chosen to play as:', playerSymbol)
    print('The computer will be playing as:', computerSymbol)
    lineBreak() 

    if playerSymbol == 'x':
        print('Therefore, you will go first.')
        
    if computerSymbol == 'x':
        print('Therefore, you will go second.')
        
    lineBreak()

    print('Type: \'TL\' for Top Left,    \'TM\' for Top Middle,    \'TR\' for Top Right,')
    print('      \'ML\' for Middle Left, \'MM\' for Middle Middle, \'MR\' for Middle Right,')
    print('      \'BL\' for Bottom Left, \'BM\' for Bottom Middle, \'BR\' for Bottom Right,')
    lineBreak()

    initialPrintBoard(dictionary=dictionaryStartBoard)
    
    while True:
        if len(dictionaryPlayerMove) == 0 or list(dictionaryPlayerMove.keys()) == '':
            print(list(dictionaryPlayerMove.keys()))
            print('No Moves Left!')
            retry = str(input('Would you like to play again?').lower())
            if retry == 'yes':
                print('Not coded yet, bye!')
                exit()
            elif retry == 'no':
                exit()
            break
        
        #Conditions for winning (Player)
        if dictionaryStartBoard['TL'] == playerSymbol and dictionaryStartBoard['ML'] == playerSymbol and dictionaryStartBoard['ML'] == playerSymbol or\
           dictionaryStartBoard['TM'] == playerSymbol and dictionaryStartBoard['MM'] == playerSymbol and dictionaryStartBoard['BM'] == playerSymbol or\
           dictionaryStartBoard['TR'] == playerSymbol and dictionaryStartBoard['MR'] == playerSymbol and dictionaryStartBoard['BR'] == playerSymbol or\
           dictionaryStartBoard['TL'] == playerSymbol and dictionaryStartBoard['TM'] == playerSymbol and dictionaryStartBoard['TR'] == playerSymbol or\
           dictionaryStartBoard['ML'] == playerSymbol and dictionaryStartBoard['MM'] == playerSymbol and dictionaryStartBoard['MR'] == playerSymbol or\
           dictionaryStartBoard['BL'] == playerSymbol and dictionaryStartBoard['BM'] == playerSymbol and dictionaryStartBoard['BR'] == playerSymbol or\
           dictionaryStartBoard['TL'] == playerSymbol and dictionaryStartBoard['MM'] == playerSymbol and dictionaryStartBoard['BR'] == playerSymbol or\
           dictionaryStartBoard['TR'] == playerSymbol and dictionaryStartBoard['MM'] == playerSymbol and dictionaryStartBoard['BL'] == playerSymbol:     
            print(playerSymbol, 'has won!')
            playagain=input('Would you like to play again?')

        #Conditions for winning (Computer)
        if dictionaryStartBoard['TL'] == computerSymbol and dictionaryStartBoard['ML'] == computerSymbol and dictionaryStartBoard['ML'] == computerSymbol or\
           dictionaryStartBoard['TM'] == computerSymbol and dictionaryStartBoard['MM'] == computerSymbol and dictionaryStartBoard['BM'] == computerSymbol or\
           dictionaryStartBoard['TR'] == computerSymbol and dictionaryStartBoard['MR'] == computerSymbol and dictionaryStartBoard['BR'] == computerSymbol or\
           dictionaryStartBoard['TL'] == computerSymbol and dictionaryStartBoard['TM'] == computerSymbol and dictionaryStartBoard['TR'] == computerSymbol or\
           dictionaryStartBoard['ML'] == computerSymbol and dictionaryStartBoard['MM'] == computerSymbol and dictionaryStartBoard['MR'] == computerSymbol or\
           dictionaryStartBoard['BL'] == computerSymbol and dictionaryStartBoard['BM'] == computerSymbol and dictionaryStartBoard['BR'] == computerSymbol or\
           dictionaryStartBoard['TL'] == computerSymbol and dictionaryStartBoard['MM'] == computerSymbol and dictionaryStartBoard['BR'] == computerSymbol or\
           dictionaryStartBoard['TR'] == computerSymbol and dictionaryStartBoard['MM'] == computerSymbol and dictionaryStartBoard['BL'] == computerSymbol:     
            print(computerSymbol, 'has won!')
            playagain = input('Would you like to play again?')
            
        if playerMove == 'START':
            del dictionaryPlayerMove[playerMove]
            print('What is your first move, player,', playerSymbol, '?')
            playerMove = str(input().upper())
        
        if computerMove == 'START':
            del dictionaryPlayerMove[computerMove]
            print('What is your first move, computer,', computerSymbol, '?')
            computerMove = str(input().upper())

#computer moves        
        if computerMove in dictionaryPlayerMove:
            lastMove = copy.deepcopy(computerMove)
            dictionaryStartBoard[lastMove] = computerSymbol
            initialPrintBoard(dictionary=dictionaryStartBoard)
            del dictionaryPlayerMove[lastMove]
            turn = 'player'
            playerMove = str(input('It is the players turn. Pick a move:\n')).upper()
            continue
                
        if computerMove not in dictionaryPlayerMove and turn == 'computer':
            print('Sorry computer. That move is not available. Your available moves are:\n', list(dictionaryPlayerMove.keys()))
            lineBreak()
            print('Please type where you would like to place your', '\'' + computerSymbol + '\'' + ' on the board.')
            lineBreak()
            computerMove = str(input('Pick a move computer\n')).upper()
            continue
            
#player moves            
        if playerMove in dictionaryPlayerMove:
            lastMove = copy.deepcopy(playerMove)
            dictionaryStartBoard[lastMove] = playerSymbol
            initialPrintBoard(dictionary=dictionaryStartBoard)
            del dictionaryPlayerMove[lastMove]
            turn = 'computer'
            computerMove = str(input('Pick your move, computer:\n')).upper()
            continue
        
        if playerMove not in dictionaryPlayerMove and turn == 'player':
            print('Sorry player. That move is not available. Your available moves are:\n', list(dictionaryPlayerMove.keys()))
            lineBreak()
            print('Please type where you would like to place your', '\'' + playerSymbol + '\'' + ' on the board.')
            lineBreak()
            playerMove = str(input('Pick a move player.\n')).upper()
            continue
              
        return

lineBreak()

TicTacToe()
