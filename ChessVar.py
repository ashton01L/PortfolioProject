# Author: Ashton Lee
# Github User: ashton01L
# Date: 12/8/2024
# Description: Create a class called ChessVar to implement an abstract board game based on a chess variant
# known as Fog of War chess.

class ChessVar:
    """
    Creates a chess game modified to have a  fog of war variant, where players can only see their own pieces and
    eligible locations of movement and attack. Certain moves, such as 'castling', 'en passant', and 'pawn promotion' are
    not allowed. There are no 'checks' or 'checkmates, but the game ends when a player's king is captured.
    """

    def __init__(self):
        """
        Initializes the game with the standard chess board setup with piece placement, initializes game state
        and starts player turn tracking.
        """
        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self._game_state = "UNFINISHED"
        self._turn = "white"

    def get_game_state(self):
        """
        Gets the value of the game_state

        :return:
            str: The value of either 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        return self._game_state

    def get_board(self, perspective):
        """
        Gets the board from the specified perspective ('white', 'black' or 'audience')

        :param:
            perspective (str): 'white', 'black', or 'audience'
        :return:
            nested list: nested list representing the board, where 'a8' is [0,0] and 'h1' is [7,7].
        """
        if perspective == "audience":
            return "[\n " + ",\n ".join(str(row) for row in self._board) + "\n]"

        hidden_board = [['*' for _ in range(8)] for _ in range(8)]
        player_pieces = 'PNBRQK' if perspective == "white" else 'pnbrqk'

        for r in range(8):
            for c in range(8):
                square = (r, c)
                piece = self._board[r][c]

                if piece in player_pieces:
                    hidden_board[r][c] = piece

                elif self._is_square_visible(square, perspective):
                    hidden_board[r][c] = piece

                elif self._board[r][c] == ' ':
                    hidden_board[r][c] = ' '

        if perspective == "white":
            return "[\n " + ",\n ".join(str(row) for row in hidden_board) + "\n]"
        else:
            # Reverse the board for black's perspective
            return "[\n " + ",\n ".join(str(row) for row in hidden_board[::-1]) + "\n]"

    def make_move(self, from_square, to_square):
        """
        Attempts to make a move from the specified square (from_square) to the target square (to_square).

        :param:
            from_square: Starting square (e.g., 'e2')
            to_square: Target square (e.g., 'e4')
        :return:
            boolean: returns 'True' if the move was successful, 'False' otherwise
        """
        if self._game_state != "UNFINISHED":
            return False

        from_row, from_col = self._algebraic_to_indices(from_square)
        to_row, to_col = self._algebraic_to_indices(to_square)
        piece = self._board[from_row][from_col]

        if not self._is_valid_turn(piece):
            return False
        if not self._is_valid_move(piece, (from_row, from_col), (to_row, to_col)):
            return False

        # Perform the move
        self._board[to_row][to_col] = piece
        self._board[from_row][from_col] = ' '
        self._update_game_state()

        # Change turn
        self._turn = "black" if self._turn == "white" else "white"
        return True

    def _is_square_visible(self, square, perspective):
        """
        Determines if the square is revealed from fog of war and visible to given player

        :param:
            square: Tuple representing the square (row, col)
            perspective: (str) 'white' or 'black'
        :return:
            boolean: returns 'True' if square has been revealed and is visible, 'False' otherwise
        """
        row, col = square
        player_pieces = 'PNBRQK' if perspective == "white" else 'pnbrqk'

        for r in range(8):
            for c in range(8):
                piece = self._board[r][c]
                if piece in player_pieces and self._can_piece_reach((r, c), square, piece):
                    return True
        return False

    def _is_valid_move(self, piece, from_square, to_square):
        """
        Checks the validity of a requested move for the given piece.

        :param:
            piece: The piece to move
            from_square: Tuple of starting coordinates (row, col)
            to_square: Tuple of target coordinates (row, col)

        :return:
            boolean: returns 'True' if the move is valid, 'False' otherwise
        """
        from_row, from_col = from_square
        to_row, to_col = to_square

        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            return False

        target_piece = self._board[to_row][to_col]
        if piece.isupper() and target_piece.isupper():
            return False
        if piece.islower() and target_piece.islower():
            return False

        return self._can_piece_reach(from_square, to_square, piece)

    def _can_piece_reach(self, from_square, to_square, piece):
        """
        Determines if a piece can legally move to a target square.

        :param:
            from_square (str): A 2 digit alphanumeric code for a board index (location)
            to_square (str): A 2 digit alphanumeric code for a board index (location)
            piece (str): A single letter string identifying the specific type of piece.

        :return:
            boolean: returns 'True' if the piece can reach, 'False' otherwise
        """
        from_row, from_col = from_square
        to_row, to_col = to_square
        dr, dc = to_row - from_row, to_col - from_col

        if piece.lower() == 'p':  # Pawn movement
            direction = -1 if piece.isupper() else 1
            start_row = 6 if piece.isupper() else 1
            if dc == 0 and self._board[to_row][to_col] == ' ':
                if dr == direction or (
                        dr == 2 * direction and from_row == start_row and self._board[from_row + direction][
                    from_col] == ' '):
                    return True
            if abs(dc) == 1 and dr == direction and self._board[to_row][to_col] != ' ':
                return True
        elif piece.lower() == 'r':
            if dr == 0 or dc == 0:
                return self._is_path_clear(from_square, to_square)
        elif piece.lower() == 'n':
            if abs(dr) == 2 and abs(dc) == 1 or abs(dr) == 1 and abs(dc) == 2:
                return True
        elif piece.lower() == 'b':
            if abs(dr) == abs(dc):
                return self._is_path_clear(from_square, to_square)
        elif piece.lower() == 'q':
            if dr == 0 or dc == 0 or abs(dr) == abs(dc):
                return self._is_path_clear(from_square, to_square)
        elif piece.lower() == 'k':
            if abs(dr) <= 1 and abs(dc) <= 1:
                return True
        return False

    def _is_path_clear(self, from_square, to_square):
        """
        Checks if the path between two squares is clear of obstacles (other pieces).

        :param:
            from_square (str): A 2 digit alphanumeric code for a board index (location)
            to_square (str): A 2 digit alphanumeric code for a board index (location)

        :return:
            boolean: returns 'True' if the path is clear, 'False' otherwise
        """
        from_row, from_col = from_square
        to_row, to_col = to_square
        dr = (to_row - from_row) // max(abs(to_row - from_row), 1)
        dc = (to_col - from_col) // max(abs(to_col - from_col), 1)
        current_row, current_col = from_row + dr, from_col + dc
        while (current_row, current_col) != (to_row, to_col):
            if self._board[current_row][current_col] != ' ':
                return False
            current_row += dr
            current_col += dc
        return True

    def _update_game_state(self):
        """
        Updates the game state if a king is captured.
        """
        white_king = any('K' in row for row in self._board)
        black_king = any('k' in row for row in self._board)

        if not white_king:
            self._game_state = "BLACK_WON"
        elif not black_king:
            self._game_state = "WHITE_WON"

    def _is_valid_turn(self, piece):
        """
        Validates if the current player can move the given piece.
        """
        return (piece.isupper() and self._turn == "white") or (piece.islower() and self._turn == "black")

    def _algebraic_to_indices(self, notation):
        """
        Converts algebraic notation to board indices.

        :param:
            square: (str) A 2 character string identifying the specific type of piece.
        """
        column, row = notation
        return 8 - int(row), ord(column) - ord('a')

    def display_board_as_list(self, board):
        """
        Prints the board in a readable nested list format.

        :param:
            board: A nested list representing the chessboard.
        """
        print("[")
        for row in board:
            print(f"  {row},")
        print("]")

# Sample game:
# game = ChessVar()
# print(game.make_move('d2', 'd4'))
# print(game.make_move('g7', 'g5'))
# print(game.make_move('c1', 'g5'))
# print(game.make_move('e7', 'e6'))
# print(game.make_move('g5', 'd8'))
# print(game.get_board("audience"))
# print(game.get_board("white"))
# print(game.get_board("black"))
