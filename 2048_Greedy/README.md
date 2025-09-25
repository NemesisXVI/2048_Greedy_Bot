# 🤖 2048 Android Automation Bot

This project automates the **2048 game** on an Android device using:
- **ADB (Android Debug Bridge)** to control the phone (screenshots + swipes).
- **OpenCV + Tesseract OCR** to detect numbers from the game board.
- **AI decision-making**:
  - A **Greedy algorithm** to maximize merges and keep the largest tile in the corner.
  - Optionally, **DeepSeek/Nebius AI API** to choose moves intelligently.

---

## 📌 Features
- Takes screenshots from Android via **ADB**.
- Detects the 2048 grid and tiles using **OpenCV**.
- Reads tile numbers using **Tesseract OCR**.
- Implements a **Greedy AI** that:
  - Keeps the **highest tile in the top-left corner**.
  - Prefers **left/up moves**.
  - Minimizes the number of tiles after each move.
- Supports **DeepSeek/Nebius AI API** to let an external AI choose moves.
- Performs swipes on the Android phone to play the game automatically.

---

## ⚙️ Environment Setup

It is recommended to use a virtual environment for this project.

### 1. Create Environment
```bash
cd 2048_Greedy
python -m venv venv
```
### 2. Activate Environment
```bash
.\venv\Scripts\Activate
```
### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Prerequisites

Before starting, make sure you have the following installed:

- **Python 3.10+** (Recommended: 3.11)
- **ADB (Android Debug Bridge)**  
  - Install from [Android Platform Tools](https://developer.android.com/tools/releases/platform-tools)  
  - Verify installation:  
    ```bash
    adb devices
    ```
- **Pipenv / Virtualenv** (to manage environments)
- **Tesseract OCR**  
  - Install from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)  
  - Verify installation:  
    ```bash
    tesseract --version
    ```
- **Python libraries**  
  Install all required dependencies using:
  ```bash
  pip install -r requirements.txt
