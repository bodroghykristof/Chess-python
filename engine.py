from string import ascii_uppercase as letters
import numpy
from pieces import *


def choose_piece(game_board, color):
    correct_input = False
    while not correct_input:
        position_string = input("Please choose your piece!")
        if check_general_correct(game_board.size, position_string) is True:
            row, column = convert_string_to_indeces(position_string)
            if own_cell(row, column, color, game_board):
                correct_input = True
    return get_piece_by_coordinates(position_string, game_board)


def check_general_correct(size, text):
    try:
        if len(text) != 2 or (int(text[1]) not in range(1, size + 1)) or (text[0].upper() not in letters[:size]):
            return False
    except ValueError:
        return False
    return True


def own_cell(row, column, color, board):
    if any(piece.position == (row, column) for piece in board.pieces_list if piece.color == color):
        return True
    return False


def empty_cell(row, column, board):
    if any(piece.position == (row, column) for piece in board.pieces_list):
        return False
    return True


def opponent_cell(row, column, color, board):
    if any(piece.position == (row, column) for piece in board.pieces_list if not piece.color == color):
        return True
    return False


def get_piece_by_coordinates(position_string, game_board):
    row, column = convert_string_to_indeces(position_string)
    for piece in game_board.pieces_list:
        if piece.position == (row, column):
            return piece


def convert_string_to_indeces(position_string):
    end_row = letters.index(position_string[0].upper())
    end_column = int(position_string[1]) - 1
    return end_row, end_column


def choose_destination(game_board, piece, color):
    correct_input = False
    while not correct_input:
        position_string = input("Please make your move!")
        if check_general_correct(game_board.size, position_string) is True:
            end_row, end_column = convert_string_to_indeces(position_string)
            if isinstance(piece, Horse) or not piece_blocks_the_way(end_row, end_column, piece, game_board):
                if piece.valid_move(piece.row, piece.column, end_row, end_column) is True and empty_cell(end_row, end_column, game_board):
                    correct_input = True
                elif piece.valid_hit(piece.row, piece.column, end_row, end_column) is True and opponent_cell(end_row, end_column, color, game_board):
                    correct_input = True
    return end_row, end_column


def piece_blocks_the_way(row, column, piece, board):
    col_difference = numpy.sign(column - piece.column)
    row_difference = numpy.sign(row - piece.row)
    if piece.row == row and any(other_piece.column in range(piece.column + col_difference, column, col_difference) and other_piece.row == row for other_piece in board.pieces_list):
        return True
    elif piece.column == column and any(other_piece.row in range(piece.row + row_difference, row, row_difference) and other_piece.column == column for other_piece in board.pieces_list):
        return True
    else:
        column_index = piece.column + col_difference
        if row_difference != 0:
            for row_index in range(piece.row + row_difference, row, row_difference):
                if any(other_piece.position == (row_index, column_index) for other_piece in board.pieces_list):
                    return True
                column_index = column_index + col_difference
    return False


def move_piece(piece, row, column):
    piece.row = row
    piece.column = column
    piece.moves += 1
    return piece


def check_hit(game_board, row, column, piece):
    for other_piece in game_board.pieces_list:
        if other_piece.row == row and other_piece.column == column and other_piece is not piece:
            game_board.pieces_list.remove(other_piece)
            del other_piece


def check_castling():
    pass


def check_pawn_finished():
    pass


def check_check(game_board, color, row, column, piece):
    king = opponent_king(game_board, color)
    if piece.valid_hit(row, column, king.row, king.column):
        return True
    return False


def opponent_king(game_board, color):
    for piece in game_board.pieces_list:
        if isinstance(piece, King) and piece.color != color:
            return piece


def check_is_win():
    return False


def switch_color(color):
    if color == "White":
        return "Black"
    return "White"
