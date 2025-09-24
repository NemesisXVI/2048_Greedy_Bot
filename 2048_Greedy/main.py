import numpy as np
import time

from game_logic import choose_best_move, check_state
from adb_functions import *
from tile_detections import resize_image, detect_grid
from deepseek_agent import choose_best_move_deepseek

SCREENSHOT_PATH = "screen.png"


def detect_game_state(image_path):
    """
    Figure out next best move based on current game state.
    """

    resized_img = resize_image(image_path)
    board = detect_grid(resized_img)
    board = np.array(board, dtype=int)
    check = check_state(board)

    if not check:
        return "", check

    # best_move = choose_best_move(board)
    best_move = choose_best_move_deepseek(board)

    if best_move == "":
        best_move = choose_best_move(board)
        print(f"Greedy suggests move: {best_move}")

    return best_move, check


def main():
    print("2048 Bot starting...")
    adb_screenshot()
    check = True
    while check:
        adb_screenshot()
        move, check = detect_game_state(SCREENSHOT_PATH)

        if not check:
            break

        print(f"Next move: {move}")
        adb_swipe(move)
        time.sleep(2)  # wait for move animation

    print("Game over or max moves reached.")
    # print(detect_game_state(SCREENSHOT_PATH))


if __name__ == "__main__":
    main()
