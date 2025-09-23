import subprocess

SCREENSHOT_PATH = "screen.png"

SWIPE_COORDS = {
    "up": (500, 1200, 500, 300),
    "down": (500, 300, 500, 1200),
    "left": (900, 800, 300, 800),
    "right": (300, 800, 900, 800)
}

def adb_call(cmd):
    full = ["adb"] + cmd
    subprocess.call(full)


def adb_screenshot():
    """Take screenshot and save to local file"""
    with open(SCREENSHOT_PATH, "wb") as f:
        subprocess.call(["adb", "exec-out", "screencap", "-p"], stdout=f)


def adb_swipe(direction):
    """Perform swipe on phone"""
    x1, y1, x2, y2 = SWIPE_COORDS[direction]
    adb_call(["shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), "100"])