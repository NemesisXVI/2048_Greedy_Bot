import numpy as np
import time

from game_logic import choose_best_move, count_tiles
from adb_functions import *
from tile_detections import resize_image, detect_grid

SCREENSHOT_PATH = "screen.png"


def detect_game_state(image_path):
    """
    Figure out next best move based on current game state.
    """

    resized_img = resize_image(image_path)
    board = detect_grid(resized_img)
    board = np.array(board, dtype=int)
    count = count_tiles(board)
    best_move = choose_best_move(board)

    return best_move, count


def main():
    print("2048 Bot starting...")
    adb_screenshot()
    count = 1
    while count <= 15:
        adb_screenshot()
        move, count = detect_game_state(SCREENSHOT_PATH)
        print(f"Next move: {move} , Count: {count}")
        adb_swipe(move)
        time.sleep(0.2)  # wait for move animation
    print("Game over or max moves reached.")
    # print(detect_game_state(SCREENSHOT_PATH))


if __name__ == "__main__":
    main()
