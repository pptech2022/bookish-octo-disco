# Global variables
from random import randint


chess_board = []
dimension = 8
rounds = 100
queen_number = 1
bishop_number = 2
rook_number = 3

def create_chess_board(dimension):
    for d in range(0, dimension):
        chess_board.append([0, 0, 0, 0, 0, 0, 0 ,0])

def print_board(dimension):
    print("| P | 1 2 3 4 5 6 7 8 |")
    print("-----------------------")
    for i in range(0, dimension):
        print("| " + str(i+1) + " | ", end = "")
        for j in range(0, dimension):
            if(chess_board[i][j] == 1):
                print("Q ", end="")
            elif(chess_board[i][j] == 2):
                print("B ", end="")
            elif(chess_board[i][j] == 3):
                print("R ", end="")
            else:
                print("x ", end="")
        print("|", end="")
        print()

def print_round(dimension, round):
    print("-----------------------")
    print("| ROUND : " + str(round+1) + "         |")
    print("-----------------------")
    print_board(dimension)
    print("-----------------------")

def check_p1(r_x_coord, r_y_coord, q_x_coord, q_y_coord, b_x_coord, b_y_coord):
    points = 0
    if(q_x_coord == r_x_coord):
        points += 1
    elif(q_y_coord == r_y_coord):
        points += 1

    if(b_x_coord > q_x_coord and b_y_coord > q_y_coord):
        while(q_x_coord < b_x_coord and b_y_coord > q_y_coord):
            q_x_coord += 1
            q_y_coord += 1
            if(q_x_coord == b_x_coord and q_y_coord == b_y_coord):
                points += 1
                break        
    elif(b_x_coord > q_x_coord and b_y_coord < q_y_coord):
        while(q_x_coord < b_x_coord and b_y_coord > q_y_coord):
            q_x_coord -= 1
            q_y_coord += 1
            if(q_x_coord == b_x_coord and q_y_coord == b_y_coord):
                points += 1
                break        
    elif(b_x_coord < q_x_coord and b_y_coord > q_y_coord):
        while(q_x_coord < b_x_coord and b_y_coord > q_y_coord):
            q_x_coord += 1
            q_y_coord -= 1
            if(q_x_coord == b_x_coord and q_y_coord == b_y_coord):
                points += 1
                break        
    elif(b_x_coord > q_x_coord and b_y_coord < q_y_coord):
        while(q_x_coord < b_x_coord and b_y_coord > q_y_coord):
            q_x_coord -= 1
            q_y_coord -= 1
            if(q_x_coord == b_x_coord and q_y_coord == b_y_coord):
                points += 1
                break        
    return points


def check_p2(r_x_coord, r_y_coord, q_x_coord, q_y_coord, b_x_coord, b_y_coord):
    points = 0
    if(q_x_coord == r_x_coord):
        points += 1
    elif(q_y_coord == r_y_coord):
        points += 1

    if(q_x_coord > b_x_coord and q_y_coord > b_y_coord):
        while(b_x_coord < q_x_coord and q_y_coord > b_y_coord):
            b_x_coord += 1
            b_y_coord += 1
            if(b_x_coord == q_x_coord and b_y_coord == q_y_coord):
                points += 1
                break        
    elif(q_x_coord > b_x_coord and q_y_coord < b_y_coord):
        while(b_x_coord < q_x_coord and q_y_coord > b_y_coord):
            b_x_coord -= 1
            b_y_coord += 1
            if(b_x_coord == q_x_coord and b_y_coord == q_y_coord):
                points += 1
                break        
    elif(q_x_coord < b_x_coord and q_y_coord > b_y_coord):
        while(b_x_coord < q_x_coord and q_y_coord > b_y_coord):
            b_x_coord += 1
            b_y_coord -= 1
            if(b_x_coord == q_x_coord and b_y_coord == q_y_coord):
                points += 1
                break        
    elif(q_x_coord > b_x_coord and q_y_coord < b_y_coord):
        while(b_x_coord < q_x_coord and q_y_coord > b_y_coord):
            b_x_coord -= 1
            b_y_coord -= 1
            if(b_x_coord == q_x_coord and b_y_coord == q_y_coord):
                points += 1
                break        
    return points
    
def play(dimension):
    player_one_points = 0
    player_two_points = 0
    create_chess_board(dimension)
    for round in range(0, rounds):
        q_x_coord = b_x_coord = r_x_coord = randint(0, 7)
        q_y_coord = b_y_coord = r_y_coord = randint(0, 7)
        chess_board[q_x_coord][q_y_coord] = queen_number
        while (chess_board[b_x_coord][b_y_coord] == queen_number):
            b_x_coord = randint(0, 7)
            b_y_coord = randint(0, 7)
        chess_board[b_x_coord][b_y_coord] = bishop_number
        while (chess_board[r_x_coord][r_y_coord] == queen_number or
        chess_board[r_x_coord][r_y_coord] == bishop_number):
            r_x_coord = randint(0, 7)
            r_y_coord = randint(0, 7)
        chess_board[r_x_coord][r_y_coord] = rook_number
        print_round(dimension, round)
        player_one_points += check_p1(r_x_coord, r_y_coord, q_x_coord, q_y_coord, b_x_coord, b_y_coord)
        player_two_points += check_p2(r_x_coord, r_y_coord, q_x_coord, q_y_coord, b_x_coord, b_y_coord)
        chess_board[q_x_coord][q_y_coord] = 0
        chess_board[b_x_coord][b_y_coord] = 0
        chess_board[r_x_coord][r_y_coord] = 0
    print("Player one points : ", player_one_points)
    print("Player two points : ", player_two_points)

play(dimension)

