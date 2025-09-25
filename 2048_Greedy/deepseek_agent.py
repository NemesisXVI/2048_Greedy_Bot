import numpy as np
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
import os


api_key = os.getenv("MY_API_KEY")
# Initialize DeepSeek client
client = OpenAI(
    api_key=str(api_key),
    base_url="https://api.studio.nebius.com/v1/"
)


def choose_best_move_deepseek(board):
    """
    Uses DeepSeek AI to decide the best move in 2048.
    """
    board = np.array(board, dtype=int).tolist()  # ensure pure list

    prompt = f"""
    You are playing the 2048 game.
    The current board is:
    {board}

    Decide the next move. Don't repeat the previous move if board doesnt change.
    Only respond with one of these words exactly: "up", "down", "left", or "right".
    """

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            ChatCompletionSystemMessageParam(role="system", content="You are an AI that plays 2048."),
            ChatCompletionUserMessageParam(role="user", content=prompt)
        ]
    )

    move = response.choices[0].message.content.strip().lower()

    print(f"DeepSeek suggests move: {move}")

    if move not in ["up", "down", "left", "right"]:
        return ""

    return move
