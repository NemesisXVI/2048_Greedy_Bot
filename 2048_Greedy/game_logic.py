import numpy as np


def compress(row):
    """Slide non-zero values to the left"""
    new_row = [x for x in row if x != 0]
    new_row += [0] * (len(row) - len(new_row))
    return new_row


def merge(row):
    """Merge equal adjacent tiles"""
    for i in range(len(row) - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return row


def move_left(board):
    new_board = []
    for row in board:
        row = compress(row)
        row = merge(row)
        row = compress(row)
        new_board.append(row)
    return np.array(new_board)


def move_right(board):
    return np.array([row[::-1] for row in move_left([row[::-1] for row in board])])


def move_up(board):
    return move_left(board.T).T


def move_down(board):
    return move_right(board.T).T


def count_tiles(board):
    return np.count_nonzero(board)

def evaluate_board(board, original_max):
    """Score a board based on greedy heuristics"""
    score = 0

    # 1. Max tile in top-left
    if board[0, 0] != original_max:
        score -= 1000  # big penalty

    # 2. Fewer tiles = better
    score -= np.count_nonzero(board)

    # 3. Monotonicity (reward decreasing rows/cols)
    # row monotonicity
    for row in board:
        for i in range(3):
            if row[i] >= row[i+1]:
                score += 1
    # col monotonicity
    for col in board.T:
        for i in range(3):
            if col[i] >= col[i+1]:
                score += 1

    return score


def choose_best_move(board):
    """Greedy: keep highest number top-left, minimize tiles"""

    original_max = board.max()
    top_left = board[0, 0]
    moves = {
        "up": move_up(board),
        "left": move_left(board),
        "right": move_right(board),
        "down": move_down(board)
    }

    best_move = None
    best_score = -float("inf")

    # Priority order: Up > Left > Right > Down
    priority = ["up", "left", "right", "down"]

    for direction in priority:
        new_board = moves[direction]
        if np.array_equal(new_board, board):
            continue  # skip invalid moves

        # Prevent moving top-left max tile away
        if top_left == original_max:
            # Any move that would move top-left tile is forbidden
            # Moving right or down may shift top-left, depending on implementation
            if direction in ["right", "down"]:
                continue
        score = evaluate_board(new_board, original_max)

        if score > best_score:
            best_score = score
            best_move = direction

    if best_move is None:
        for direction in priority:
            new_board = moves[direction]
            if not np.array_equal(new_board, board):
                best_move = direction
                break

    return best_move
