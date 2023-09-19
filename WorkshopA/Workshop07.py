import random

def create_bingo_board():
    board = []
    for _ in range(5):
        row = random.sample(range(1, 26), 5)
        board.append(row)
    return board

def display_bingo_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def play_bingo():
    print("ยินดีต้อนรับสู่เกม Bingo!")
    bingo_board = create_bingo_board()
    display_bingo_board(bingo_board)
    
    while True:
        try:
            guess = int(input("ทายตัวเลข (1-25): "))
            if guess < 1 or guess > 25:
                print("โปรดป้อนตัวเลขระหว่าง 1 ถึง 25")
            else:
                break
        except ValueError:
            print("โปรดป้อนตัวเลขที่ถูกต้อง")

    if guess in set(sum(bingo_board, [])):
        print("Correct, You are the winner!")
    else:
        print("Not Correct !!!")

play_bingo()