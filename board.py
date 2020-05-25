class Board:
    def __init__(self, size, color_one, color_two, row_marks, column_marks):
        self.size = size
        self.color_one = color_one
        self.color_two = color_two
        self.row_marks = row_marks
        self.column_marks = column_marks
        self.pieces_list = []

    def display(self):
        print(" ", end=" ")
        for column_index in range(self.size):
            print(self.column_marks[column_index], end=" ")
        print()
        for row_index in range(self.size):
            print(self.row_marks[row_index], end=" ")
            for column_index in range(self.size):
                for piece in self.pieces_list:
                    if piece.row == row_index and piece.column == column_index:
                        print(piece.mark, end=" ")
                        break
                else:
                    print(" ", end=" ")
            print()