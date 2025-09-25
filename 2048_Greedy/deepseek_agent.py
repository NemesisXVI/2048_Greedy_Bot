import numpy as np
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam



# Initialize DeepSeek client
client = OpenAI(
    api_key="eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTE3NTM2MDEyNDk0MjYxNzAyMSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkxNjQ3OTAxNCwidXVpZCI6IjAxOTk4MDk3LTMzMGEtNzZlZi04NTgxLWNjZDQzMGY1YTBkZiIsIm5hbWUiOiIzcmQiLCJleHBpcmVzX2F0IjoiMjAzMC0wOS0yNFQxMToxNjo1NCswMDAwIn0.7yTBCavlBERBGOa4HlbFVyjA1wCKkMH5YQ4jUPcCcOY",
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
