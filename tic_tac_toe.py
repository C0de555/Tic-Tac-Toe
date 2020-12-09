class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print(self):
        print(self.cells[1], '|', self.cells[2], '|', self.cells[3])
        print("----------")
        print(self.cells[4], '|', self.cells[5], '|', self.cells[6])
        print("----------")
        print(self.cells[7], '|', self.cells[8], '|', self.cells[9])

    def update_board(self, cell_number, player):
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player

    def cell_taken(self, cell_number):
        if cell_number != " ":
            return True
        else:
            return False

    def winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

    def tie(self):
        cells_left = 9
        for cell in self.cells:
            if cell != " ":
                cells_left -= 1
        if cells_left == 0:
            return True
        else:
            return False


# Welcome message
print("Welcome to the virtual tic-tac-toe game!")
print("Player 1 will be 'X' and Player 2 will be 'O'")

board = Board()

while True:
    board.print()

    # player 1 plays
    print("Player 1, it's your turn")
    # get valid input
    player1_move = int(input("Where would you like to move (1-9): "))

    # update board
    board.update_board(player1_move, 'X')
    
    # check to see if player 1 won
    if board.winner("X") is True:
        print("Player 1 is the winner!")
        exit()
    # check to see if it's a tie game
    if board.tie() is True:
        print("It's a tie!")
        exit()

    # player 2 plays
    print("Player 2, it's your turn")
    # get input
    player2_move = int(input("Where would you like to move (1-9): "))
   
    # update board
    board.update_board(player2_move, 'O')
    
    # check to see if player 2 won
    if board.winner("O") is True:
        print("Player 2 is the winner!")
        exit()
