from piece import Piece

class ConnectBoard:
    def __init__(self) -> None:
        self.WIDTH = 7
        self.HEIGHT = 6
        self.board = [[Piece.Empty for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.last_piece = Piece.Black

    def __str__(self) -> str:
        return "\n".join(" ".join(str(piece.value) for piece in row) for row in self.board)

    def __repr__(self) -> str:
        return str(self)

    def drop_piece(self, column: int) -> bool:
        piece = Piece.Red if self.last_piece == Piece.Black else Piece.Black
        # Column is out of bounds
        if column < 0 or column >= self.WIDTH:
            return False

        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][column] == Piece.Empty:
                self.board[row][column] = piece
                self.last_move = (row, column)
                self.last_piece = piece
                return True
        return False

    def check_win(self) -> bool:
        return self.check_horizontal() or self.check_vertical() or self.check_diagonal()

    def check_horizontal(self) -> bool:
        countLeft = 0
        countRight = 0

        # Count left
        for col in range(self.last_move[1] - 1, -1, -1):
            if self.board[self.last_move[0]][col] == self.last_piece:
                countLeft += 1
            else:
                break

        # Count right
        for col in range(self.last_move[1] + 1, self.WIDTH):
            if self.board[self.last_move[0]][col] == self.last_piece:
                countRight += 1
            else:
                break

        win = countLeft + countRight >= 3
        if win:
            self.winCondition = "Horizontal"
        return win

    def check_vertical(self) -> bool:
        countDown = 0
        countUp = 0

        # Count down
        for row in range(self.last_move[0] -1, -1, -1):
            if self.board[row][self.last_move[1]] == self.last_piece:
                countDown += 1
            else:
                break

        # Count up
        for row in range(self.last_move[0] + 1, self.HEIGHT):
            if self.board[row][self.last_move[1]] == self.last_piece:
                countUp += 1
            else:
                break

        win = countDown + countUp >= 3
        if win:
            self.winCondition = "Vertical"
        return win


    def check_diagonal(self):
        return self.check_diagonal_left() or self.check_diagonal_right()

    def check_diagonal_left(self) -> bool:
        countDown = 0
        countUp = 0

        # Count down
        for row, col in zip(range(self.last_move[0] -1, -1, -1), range(self.last_move[1]-1, -1, -1)):
            if self.board[row][col] == self.last_piece:
                countDown += 1
            else:
                break

        # Count up
        for row, col in zip(range(self.last_move[0] + 1, self.HEIGHT), range(self.last_move[1]+1, self.WIDTH)):
            if self.board[row][col] == self.last_piece:
                countUp += 1
            else:
                break

        win = countDown + countUp >= 3
        if win:
            self.winCondition = "Diagonal Left"
        return win


    def check_diagonal_right(self) -> bool:
        countDown = 0
        countUp = 0

        # Count down
        for row, col in zip(range(self.last_move[0]-1, -1, -1), range(self.last_move[1]+1, self.WIDTH)):
            if self.board[row][col] == self.last_piece:
                countDown += 1
            else:
                break

        # Count up
        for row, col in zip(range(self.last_move[0]+1, self.HEIGHT), range(self.last_move[1]-1, -1, -1)):
            if self.board[row][col] == self.last_piece:
                countUp += 1
            else:
                break

        win = countDown + countUp >= 3
        if win:
            self.winCondition = "Diagonal Right"
        return win