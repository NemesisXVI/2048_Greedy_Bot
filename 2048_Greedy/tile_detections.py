import cv2
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r"E:\Tesseract\tesseract.exe"


def resize_image(image_path):
    """Check if image can be opened and resize for faster processing"""
    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load image.")
        return None
    else:
        print("Image loaded successfully, shape:", img.shape)
        scale_percent = 400 / img.shape[1]  # 800 px width
        new_width = int(img.shape[1] * scale_percent)
        new_height = int(img.shape[0] * scale_percent)
        resized_img = cv2.resize(img, (new_width, new_height))

        return resized_img


def detect_grid(img):
    """Detect 2048 grid and tiles"""

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    grid_contour = max(contours, key=cv2.contourArea)
    img_contour = img.copy()
    # cv2.drawContours(img_contour, [grid_contour], -1, (0, 0, 255), 3)
    # cv2.imshow("Grid Detected", img_contour)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    x, y, w, h = cv2.boundingRect(grid_contour)
    tile_w = w // 4
    tile_h = h // 4

    tiles = []
    for i in range(4):
        row = []
        for j in range(4):
            x0 = x + j * tile_w
            y0 = y + i * tile_h
            tile_img = img[y0:y0 + tile_h, x0:x0 + tile_w]
            tile_value = detect_tile_value(tile_img)
            row.append(tile_value)
        tiles.append(row)
    print(tiles)
    return tiles


def detect_tile_value(tile_img):
    """Use OCR to detect tile value"""
    gray_tile = cv2.cvtColor(tile_img, cv2.COLOR_BGR2GRAY)
    gray_tile = crop_tile_inner(gray_tile)

    # cv2.imshow( "tile",gray_tile)
    # cv2.waitKey(900)
    # cv2.destroyAllWindows()

    config = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"
    text = tess.image_to_string(gray_tile, config=config).strip()
    if text in ["2", "4"]:
        return text
    gray_inverted = cv2.bitwise_not(gray_tile)
    text = tess.image_to_string(gray_inverted, config=config).strip()

    return text if text.isdigit() else "0"


def crop_tile_inner(tile_img, border_ratio=0.15):
    """Crop the inner part of a tile to remove borders"""
    h, w = tile_img.shape[:2]
    top = int(h * border_ratio)
    bottom = int(h * (1 - border_ratio))
    left = int(w * border_ratio)
    right = int(w * (1 - border_ratio))
    return tile_img[top:bottom, left:right]
