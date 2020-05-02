# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:11:09 2020

@author: Kat
"""
#RUNNING MANY GAMES TO SEE THE BETTER COMPUTER METHOD

def main():
    import numpy as np
    import random
    
    #game board, 8 x 8
    def start_board(): #Create the board set-up with pieces in starting position
        board = []
        for i in range(8):
            board.append([' '] * 8) # 8 rows made of 8 empty strings. 
        board[0][1] = 'O'
        board[0][3] = 'O'
        board[0][5] = 'O'
        board[0][7] = 'O'
        board[1][0] = 'O'
        board[1][2] = 'O'
        board[1][4] = 'O'
        board[1][6] = 'O'
        board[2][1] = 'O'
        board[2][3] = 'O'
        board[2][5] = 'O'
        board[2][7] = 'O'
        board[5][0] = 'X'
        board[5][2] = 'X'
        board[5][4] = 'X'
        board[5][6] = 'X'
        board[6][1] = 'X'
        board[6][3] = 'X'
        board[6][5] = 'X'
        board[6][7] = 'X'
        board[7][0] = 'X'
        board[7][2] = 'X'
        board[7][4] = 'X'
        board[7][6] = 'X'
        return board

    #this contains the "rules" for what kinds of moves are allowed.        
    def valid_move_rules(board, marker, marker_king, xstart, ystart): 
        #is a move to this space by this player legal? 
        #should return true is this move can be made
        #define player's and opponent's pieces
        if marker == 'X': 
            opponent = 'O'
            opponent_king = '0'
            player = 1
        elif marker == 'O':
            opponent = 'X'
            opponent_king = 'K'
            player = 2  
        piece = board[xstart][ystart] #assigns a marker to the piece
        #start move scenario to check if there are legal moves to make
        moves_to_make = [] 
        mandatory_moves_to_make = []
        piece_to_capture = [] #if a move to make jumps over and captures a piece, the piece captured will be the move -1 in the direction it came grom and that space will be changed to empty
        if player == 1:
            if piece == marker: #piece is a pawn, can only move forward (up for X's)
                for xdirection, ydirection in [ [-1,-1], [-1,1]]: #the 2 ways this piece could moveS
                    x = xstart
                    y = ystart
                    x = x + xdirection #check for diag moves
                    y = y + ydirection
                    if is_on_board(x, y) and board[x][y] == ' ':
                        moves_to_make.append([x, y])
                    elif is_on_board(x, y) and board[x][y] in (opponent, opponent_king): #move one more space in that direction to see if the piece can be jumped
                        xjump = x + xdirection 
                        yjump = y + ydirection
                        if is_on_board(xjump, yjump) and board[xjump][yjump] == ' ':
                            moves_to_make.append([xjump, yjump])
                            mandatory_moves_to_make.append([xjump, yjump])
                            piece_to_capture.append([x, y]) #this stores the location of the capturable piece so it can be changed to ' ' later
            elif piece == marker_king: #piece is a king and can  move in diag. forwards and back. 
                for xdirection, ydirection in [ [-1,-1], [1,-1], [-1,1], [1,1]]: #the 4 ways this piece could moveS
                    x = xstart
                    y = ystart
                    x = x + xdirection #check for diag moves
                    y = y + ydirection
                    if is_on_board(x, y) and board[x][y] == ' ':
                        moves_to_make.append([x, y])
                    elif is_on_board(x, y) and board[x][y] in (opponent, opponent_king):
                        xjump = x + xdirection 
                        yjump = y + ydirection
                        if is_on_board(xjump, yjump) and board[xjump][yjump] == ' ':
                            moves_to_make.append([xjump, yjump])
                            mandatory_moves_to_make.append([xjump, yjump])
                            piece_to_capture.append([x, y])
        #player 2 can only move down the board so the x and y directions must be changed. 
        elif player == 2:
            if piece == marker: 
                for xdirection, ydirection in [ [1,-1], [1,1]]:
                    x = xstart
                    y = ystart
                    x = x + xdirection 
                    y = y + ydirection
                    if is_on_board(x, y) and board[x][y] == ' ':
                        moves_to_make.append([x, y])
                    elif is_on_board(x, y) and board[x][y] in (opponent, opponent_king):
                        xjump = x + xdirection 
                        yjump = y + ydirection
                        if is_on_board(xjump, yjump) and board[xjump][yjump] == ' ':
                            moves_to_make.append([xjump, yjump])
                            mandatory_moves_to_make.append([xjump, yjump])
                            piece_to_capture.append([x, y])     
            elif piece == marker_king: #piece is a king, can move forwards and backwards 
                for xdirection, ydirection in [ [-1,-1], [1,-1], [-1,1], [1,1]]: 
                    x = xstart
                    y = ystart
                    x = x + xdirection 
                    y = y + ydirection
                    if is_on_board(x, y) and board[x][y] == ' ':
                        moves_to_make.append([x, y])
                    elif is_on_board(x, y) and board[x][y] in (opponent, opponent_king):
                        xjump = x + xdirection 
                        yjump = y + ydirection
                        if is_on_board(xjump, yjump) and board[xjump][yjump] == ' ':
                            moves_to_make.append([xjump, yjump])
                            mandatory_moves_to_make.append([xjump, yjump])
                            piece_to_capture.append([x, y])
        if len(moves_to_make) == 0:
            return False #there were no valid moves
        return (piece_to_capture, moves_to_make, mandatory_moves_to_make)
    
    def is_move_valid(board, marker, marker_king, xstart, ystart): 
        if valid_move_rules(board, marker, marker_king, xstart, ystart) != False:
            piece_to_capture, moves_to_make, mandatory_moves_to_make = valid_move_rules(board, marker, marker_king, xstart, ystart)
            if len(moves_to_make) == 0:
                return False
            else:
                return moves_to_make
        else:
            return False
        
    def get_possible_moves(board, marker, marker_king):
        #creates a list of ALL the possible moves this player can make 
        #need to show only jump moves in the event of a jump opportunity
        possible_moves = []
        mandatory_moves = []
        for x in range(8):
            for y in range(8):
                if is_move_valid(board, marker, marker_king, x, y) != False: #this will look at every space on the board check if a move to this location would be a legal using the is move valid function. 
                    #if false, then there is no valid move to that space. 
                    piece_to_capture, moves_to_make, mandatory_moves_to_make = valid_move_rules(board, marker, marker_king, x,y)
                    possible_moves = possible_moves + moves_to_make #this creates a list of all the possible moves. 
                    mandatory_moves = mandatory_moves + mandatory_moves_to_make
        if len(mandatory_moves) != 0:
            possible_moves = mandatory_moves
        return possible_moves
    
    def get_movable_pieces(board, marker, marker_king):
        #creates a list of all the possible moves this player can make 
        #need to show only jump moves in the event of a jump opportunity
        movable_pieces = []
        mandatory_pieces = []
        for x in range(8):
            for y in range(8):
                if is_move_valid(board, marker, marker_king, x, y) != False: #this will look at every space on the board check if a move to this location would be a legal using the is move valid function. 
                    #if false, then there is no valid move to that space. 
                    movable_pieces.append([x,y]) #this creates a list of all the possible moves. 
                    piece_to_capture, moves_to_make, mandatory_moves_to_make = valid_move_rules(board, marker, marker_king, x,y)
                    if len(mandatory_moves_to_make) != 0:
                        mandatory_pieces.append([x,y])
        if len(mandatory_pieces) != 0:
                movable_pieces = mandatory_pieces
        for x in range(8):
            for y in range(8):
                for x, y in movable_pieces:
                    if x > (x+1) or x < (x-1): #if the x val changes by more than 1, that means a piece could be jumped
                        mandatory_pieces.append([x,y])
        if len(mandatory_pieces) != 0:
            movable_pieces = mandatory_pieces
        return movable_pieces
    
    def make_move(board, marker, marker_king, xstart, ystart, xnew, ynew):        
        if board[xstart][ystart] == marker:
            board[xnew][ynew] = marker
            board[xstart][ystart] = ' '
        if board[xstart][ystart] == marker_king:
            board[xnew][ynew] = marker_king
            board[xstart][ystart] = ' '
    
    def capture_piece(board, marker, marker_king, xstart, ystart, xnew, ynew):
        #give location of piece that was captured
        if xnew == (xstart + 2):
            if ynew == (ystart + 2):
                board[(xstart+1)][(ystart+1)] = ' '
            if ynew == (ystart - 2):
                board[(xstart+1)][(ystart-1)] = ' '
        elif xnew == (xstart - 2):
            if ynew == (ystart + 2):
                board[(xstart-1)][(ystart+1)] = ' '
            if ynew == (ystart - 2):
                board[(xstart-1)][(ystart-1)] = ' '
        #this will be part of updating the board during gameplay
     
    def opposite_end(marker, xnew, ynew):
        #has the player's piece reached the opposite end of the board? true for p1 if in row 0 and for p2 if in row 7. This is part 1 of determining if the piece will become a king
        #note*limiting the piece to one that is not already a king prevents the computer from just moving one king piece back and forth the whole time
        if marker == 'X':
            if xnew == 0:
                return True
            else:
                return False
        if marker == 'O':
            if xnew == 7:
                return True
            else:
                return False
        
    def piece_becomes_king(board, marker, marker_king, xstart, ystart, xnew, ynew):
        #if the piece has reached the end of the board, it will become a king. If this is true, then in the gameplay, we will create an if loop where if this is true, then marker becomes marker_king. 
        if board[xstart][ystart] == marker_king:
            return False
        if opposite_end(marker, xnew, ynew) == True:
            board[xnew][ynew] = marker_king
            return True   #keeps pieces that are already kings from being marked as becoming a king      
    
    def get_computer_move_1(board, marker, marker_king):
        pieces = get_movable_pieces(board, marker, marker_king) 
        move_info = [] #this will contain the position of both the piece start and end location for a move. 
        king_move_info = [] #groups moves that would give the player a king piece
        for x, y in pieces:
            xstart = x
            ystart = y
            piece = [xstart, ystart]
            if valid_move_rules(board, marker, marker_king, xstart, ystart) == False:
                break
            piece_to_capture, moves_to_make, mandatory_moves_to_make = valid_move_rules(board, marker, marker_king, xstart, ystart)
            if len(mandatory_moves_to_make) != 0:
                moves_to_make = mandatory_moves_to_make
            for x, y in moves_to_make:
                xnew = x
                ynew = y
                move = [xnew, ynew]
                move_info.append([piece, move]) #many pieces will have two moves that they can make. This way, if a piece can make 2 moves, there will be a [piece,move] for each
                if piece_becomes_king(board, marker, marker_king, xstart, ystart, xnew, ynew) == True:
                    king_move_info.append([piece, move])
        if len(king_move_info) != 0:
            move_info = king_move_info #A move that will get the computer a king piece will always be chosen if available and legal to make.
        [xstart, ystart], [xnew, ynew] = random.choice(move_info) #this will pick a random move in the list of move_info. A move that will get the computer a king piece. It will also redefine and select the computer's x/y start and end ('new') values
        return xstart, ystart, xnew, ynew
    
    def get_computer_move_2(board, marker, marker_king):
        pieces = get_movable_pieces(board, marker, marker_king) 
        move_info = [] 
        end_space = []
        #move pieces toward the middle and help the computer control the center of the board
        for x, y in pieces:
            xstart = x
            ystart = y
            piece = [xstart, ystart]
            piece_to_capture, moves_to_make, mandatory_moves_to_make = valid_move_rules(board, marker, marker_king, xstart, ystart)
            if len(mandatory_moves_to_make) != 0:
                moves_to_make = mandatory_moves_to_make
            for x, y in moves_to_make:
                xnew = x
                ynew = y
                move = [xnew, ynew]
                move_info.append([piece, move])
        for x in range(len(move_info)):
            end_space.append(move_info[x][1])
        #find which move will put the player closest to the center 
        center = [3,4] #approx center of board
        end = np.array(end_space)#make a copy of end_space
        end = np.abs(end - center) #get list of closeness to center
        end = np.min(end, axis=1)
        find = np.min(end, axis=0) #which one is closest
        val = end.tolist().index(find) #pull location of closest end space in list
        [xstart, ystart], [xnew, ynew] = move_info[val] #use location to get closet ending move
        return xstart, ystart, xnew, ynew
    
    def get_computer_move(comp_level, board, marker, marker_king):
        if comp_level == 1:
            xstart, ystart, xnew, ynew = get_computer_move_1(board, marker, marker_king)
        if comp_level == 2:
            xstart, ystart, xnew, ynew = get_computer_move_2(board, marker, marker_king)
        return xstart, ystart, xnew, ynew
    
    def get_winner(board):
        #how many pieces are left on the board...
        player1_pieces = 0
        player2_pieces = 0 
        for x in range (8):
            for y in range(8):
                if board[x][y] == 'X':
                    player1_pieces = player1_pieces + 1
                if board[x][y] == 'K':
                    player1_pieces = player1_pieces + 2
                    #this is because in checkers, a 'king' piece is 2 stacked regular pieces. so you essentiall win back a piece
                if board[x][y] == 'O':
                    player2_pieces = player2_pieces + 1
                if board[x][y] == '0':
                    player2_pieces = player2_pieces + 2
        if player2_pieces > player1_pieces:
            winner = 'Player 2 wins!'
        if player2_pieces < player1_pieces:
            winner = 'Player 1 wins!'
        elif player2_pieces == player1_pieces:
            winner = "It's a tie!"
        return winner
    
    
    ###################################################################
   
    player1_type = 'comp'
    p1comp_level = 1
    player2_type = 'comp'
    p2comp_level = 2
        
    player1_marker = 'X'
    player2_marker = 'O'
    player1_marker_king = 'K'
    player2_marker_king = '0'

    turn = 1 
    game_board = start_board()
    game_over = False 
    
    while not game_over:
        if (turn % 2) != 0: #first turn is 1, which is odd. 
            possible_moves = get_possible_moves(game_board, player1_marker, player1_marker_king)
            if len(possible_moves) == 0:
                game_over = True
                break      
            if player1_type == 'human': #get the human's move
                pass
            if player1_type == 'comp':
                xstart, ystart, xnew, ynew = get_computer_move(p1comp_level, game_board, player1_marker, player1_marker_king)
            make_move(game_board, player1_marker, player1_marker_king, xstart, ystart, xnew, ynew)
            capture_piece(game_board, player1_marker, player1_marker_king, xstart, ystart, xnew, ynew)
            piece_becomes_king(game_board, player1_marker, player1_marker_king, xstart, ystart, xnew, ynew)
            turn = turn + 1
        if (turn % 2) == 0:
            possible_moves = get_possible_moves(game_board, player2_marker, player2_marker_king)
            if len(possible_moves) == 0:
                game_over = True
                break
            if player2_type == 'human':
                pass
            if player2_type == 'comp': 
                xstart, ystart, xnew, ynew = get_computer_move(p2comp_level, game_board, player2_marker, player2_marker_king)
            make_move(game_board, player2_marker, player2_marker_king, xstart, ystart, xnew, ynew)
            capture_piece(game_board, player2_marker, player2_marker_king, xstart, ystart, xnew, ynew)
            piece_becomes_king(game_board, player2_marker, player2_marker_king, xstart, ystart, xnew, ynew)
            turn = turn + 1        
    winner = get_winner(game_board)
    return winner

p1wins = 0
p2wins = 0
tie = 0

for i in range(100):
    winner =  main()
    gamenum = i + 1
    if winner == 'Player 1 wins!':
        p1wins = p1wins + 1
    if winner == 'Player 2 wins!':
        p2wins = p2wins + 1
    else:
        tie = tie + 1

print(gamenum, 'games. p1 won', p1wins, 'p2 won', p2wins)









