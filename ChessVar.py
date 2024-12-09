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

        # initializes the board with standard chess setup
        self._board = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        self._game_state = "UNFINISHED"
        self._turn = "white"

    def get_game_state(self):
        """
        Gets the value of the game_state

        :return:
            str: The value of either 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        pass

    def get_board(self, perspective):
        """
        Gets the board from the specified perspective ('white', 'black' or 'audience')

        :param:
            perspective (str): 'white', 'black', or 'audience'
        :return:
            nested list: nested list representing the board, where 'a8' is [0,0] and 'h1' is [7,7].
        """
        pass

    def make_move(self, from_square, to_square):
        """
        Attempts to make specified piece on from_square move to to_square

        :param:
            from_square: starting square
            to_square: target square
        :return:
            boolean: returns 'True' if the move was successful, 'False' otherwise
        """
        pass

    def _is_square_visible(self, square, perspective):
        """
        Determines if the square is revealed from fog of war and visible to given player

        :param:
            square: Tuple representing the square (row, col)
            perspective: (str) 'white' or 'black'
        :return:
            boolean: returns 'True' if square has been revealed and is visible, 'False' otherwise
        """
        pass

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
        pass

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
        pass

    def _is_path_clear(self, from_square, to_square):
        """
        Checks if the path between two squares is clear of obstacles (other pieces).

        :param:
            from_square (str): A 2 digit alphanumeric code for a board index (location)
            to_square (str): A 2 digit alphanumeric code for a board index (location)

        :return:
            boolean: returns 'True' if the path is clear, 'False' otherwise
        """
        pass

    def _update_game_state(self):
        """
        Updates the game state if a king is captured and based on the board.
        """
        pass

    def _is_valid_turn(self, piece):
        """
        Checks if the current player can move the given piece.

        :param:
            piece (str): A single letter string identifying the specific type of piece.
        """
        pass

    def _algebraic_to_indices(self, square):
        """
        Converts algebraic notation to board indices.

        :param:
            square: (str) A 2 character string identifying the specific type of piece.
        """
        pass

    def _indices_to_algebraic(self, row, col):
        """
        Converts board indices to algebraic notation

        :param:
            row: (chr) The row of the square
            col: (ord) THE column of the square
        :return:
            Returns an algebraic notation based on correlation to square via corresponding row, col
        """

    # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

    # INTIALIZING THE GAME THROUGH THE ChessVar class: In my Fog of War Chess game, the board, game_state and player
    # turn are initialized by through the init constructor. Assignment of first turn is to the white player. This
    # creates a ChessVar instance.

    # GAME LOOP:
    # A 'make_move' input is provided, then a 'get_game_state' check is called to see if the game has not been won.
    # The move is then validated to check if the starting square is valid for the current player's pieces and then
    # the move is checked for legality according to rules for the piece. If the move is deemed valid, then update
    # the board by moving the piece and removing any captured piece. Then update visibility by hiding opponents
    # pieces unless they sit in a visible square. Then check for end of game and update game_state if necessary. If
    # game continues, switch player turn to opponent and output 'True' if successful, 'False' otherwise. For current
    # board view, input get_board() and which perspective desired, acceptable inputs are 'white', 'black' or
    # 'audience'. Return the board state, respectfully, for the desired input, hiding opponents non-visible pieces
    # or for audience, show full board. Check game state via getter, with expected return as a string. Loop until
    # gamed_state returns 'WHITE_WON' or 'BLACK_WON'

    # VISUALIZING THE BOARD: This is done through the get_board() method, which when called, will return a nested
    # list showing 8 rows (8-1, from top to bottom) and 8 columns (a-h, from left to right), which also corresponds
    # in the following manner: Column: 'a' -> 0, 'b' -> 1, ... and Row: '8' -> 0, '7' -> 1, ... to allow for
    # conversion to indices.

    # GET CURRENT STATE OF GAME: This will be done through a simple getter method 'get_game_state' to pull current
    # game_state which is updated after each player turn throughout the game, via the '_update_game_state()' method.
    # Since game_state will be set to 'UNFINISHED' at launch, status will only change through '_update_game_state'
    # method.

    # UPDATING GAME STATE: Reviews current state of board to verify that both 'white king' and 'black king' are
    # present. If either is not present, declares other as winner.

    # DETERMINING VISIBILITY THROUGH FOG OF WAR: accepts 2 parameters, 'square' and 'perspective'
    # First determines which piece and from which player, then determines if specified piece can reach through the
    # '_can_piece_reach()' method. If piece can reach, returns 'True' if visible, 'False' otherwise

    # MAKING PIECES MOVE:  accepts 2 parameters, 'from_square' and 'to_square'
    # Pieces are moved by defining starting square of piece and defining the target square of
    # piece specified by location of starting square. For instance, make_move() method accepts 2 inputs. Whatever
    # the first input is will determine the piece being moved. That piece will be identified and then the piece
    # will be checked if move to target square is valid, through the '_is_valid_move()' method. Application
    # will return 'False' and reject the move if not valid, otherwise continue logic flow if valid. Once validity is
    # confirmed, legality of move will be checked via the '_can_piece_reach()' method. This method accepts 3 inputs
    # 'from_square', 'to_square' and 'piece'. Since the 'piece' will be known at this point, the '_is_path_clear()'
    # method can be called to ensure path is clear of obstacles. Opponents pieces, when targeted, will be identified
    # and validated as capturable targets through the '_is_valid_move()' and '_is_valid_turn() and captured in the
    # 'make_move() method. If move attacks an opponent piece, opponent piece will be captured. As long as move is
    # valid the piece will be moved to its new location, '_update_game_state() method will be called and the turn
    # will be cycled to the other player.

    # DETERMINING WHEN GAME IS OVER:
    # Upon '_update_game_state()', if either king is found to not be on the board, game is declared over and winner
    # is indicated for the player who still has king piece on board.