class Piece:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.moves = []

    @property
    def position(self):
        return self.row, self.column

    @position.setter
    def position(self, coordinates):
        self.row = coordinates[0]
        self.column = coordinates[1]


class Bishop(Piece):
    def __init__(self, row, column, color):
        self.mark = "B"
        super().__init__(row, column, color)

    def valid_move(self, start_row, start_col, end_row, end_col):
        if start_row == end_row or start_col == end_col:
            return True
        return False


class Horse(Piece):
    def __init__(self, row, column, color):
        self.mark = "H"
        super().__init__(row, column, color)

    def valid_move(self, start_row, start_col, end_row, end_col):
        if sorted([abs(start_row - end_row), abs(start_col - end_col)]) == [1, 2]:
            return True
        return False


class Rook(Piece):
    def __init__(self, row, column, color):
        self.mark = "R"
        super().__init__(row, column, color)

    def valid_move(self, start_row, start_col, end_row, end_col):
        if abs(start_row - end_row) == abs(start_col - end_col):
            return True
        return False


class Queen(Piece):
    def __init__(self, row, column, color):
        self.mark = "Q"
        super().__init__(row, column, color)

    def valid_move(self, start_row, start_col, end_row, end_col):
        rook = Rook(start_row, start_col, "")
        bishop = Bishop(start_row, start_col, "")
        if rook.valid_move(start_row, start_col, end_row, end_col) or bishop.valid_move(start_row, start_col, end_row, end_col):
            return True
        return False


class King(Piece):
    def __init__(self, row, column, color):
        self.mark = "K"
        super().__init__(row, column, color)

    def valid_move(self, start_row, start_col, end_row, end_col):
        if sorted([abs(start_row - end_row), abs(start_col - end_col)]) in ([0, 1], [1, 1]):
            return True
        return False


class Pawn(Piece):
    def __init__(self, row, column, color):
        self.mark = "P"
        super().__init__(row, column, color)

    def valid_move(self, start_row, start_col, end_row, end_col):
        if end_row - start_row == -1 and self.color == "White":
            return True
        elif end_row - start_row == 1 and self.color == "Black":
            return True
        return False


DEFAULT_SETUP_BLACK = [Bishop, Horse, Rook, King, Queen, Rook, Horse, Bishop]
DEFAULT_SETUP_WHITE = [Bishop, Horse, Rook, Queen, King, Rook, Horse, Bishop]


def create_pieces(board):
    for row_index in range(board.size):
        for column_index in range(board.size):
            if row_index == 0:
                board.pieces_list.append(DEFAULT_SETUP_BLACK[column_index](row_index, column_index, "Black"))
            elif row_index == 1:
                board.pieces_list.append(Pawn(row_index, column_index, "Black"))
            elif row_index == board.size - 2:
                board.pieces_list.append(Pawn(row_index, column_index, "White"))
            elif row_index == board.size - 1:
                board.pieces_list.append(DEFAULT_SETUP_WHITE[column_index](row_index, column_index, "White"))