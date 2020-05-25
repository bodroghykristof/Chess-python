import engine
from board import *
from pieces import *
import os


DEFAULT_ROW_MARKS = ["A", "B", "C", "D", "E", "F", "G", "H"]
DEFAULT_COLUMN_MARKS = [str(i) for i in range(1, 9)]


def main():
    board_size = 8
    game_board = Board(board_size, "White", "Black", DEFAULT_ROW_MARKS, DEFAULT_COLUMN_MARKS)
    create_pieces(game_board)
    color = "White"

    while not engine.check_is_win():
        game_board.display()
        print(color)
        print("OK")
        piece = engine.choose_piece(game_board, color)
        row, column = engine.choose_destination(game_board, piece, color)
        piece = engine.move_piece(piece, row, column)
        engine.check_hit(game_board, row, column, piece)
        engine.check_castling()
        engine.check_pawn_finished()
        engine.check_check(game_board, color, row, column, piece)
        engine.check_is_win()
        color = engine.switch_color(color)
        os.system('clear')


if __name__ == '__main__':
    main()
