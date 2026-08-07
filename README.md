# auto_game

以 OpenCV 影像模板比對辨識遊戲畫面按鈕，再透過 `pyautogui` 自動點擊，實現遊戲流程自動化（自動開始、自動結束、自動重複遊戲）。

Game automation script that captures the screen via OpenCV, locates on-screen buttons/icons using template matching, and drives mouse clicks with `pyautogui` to automatically start, play, and restart a game loop.

## 功能 / Features

- **畫面擷取**：透過 `cv2.VideoCapture` 讀取遊戲畫面（如虛擬攝影機/擷取卡輸出）。
  Captures the game display via `cv2.VideoCapture` (e.g. from a capture card or virtual camera).
- **模板比對辨識**：使用 `cv2.matchTemplate` 比對按鈕圖示（`start_game_play.jpg`、`end_game.jpg`、`butten_X.jpg` 等）在畫面中的位置。
  Uses `cv2.matchTemplate` to locate button icons (start/end/close buttons, etc.) on screen.
- **自動點擊**：辨識成功後以 `pyautogui` 移動滑鼠並點擊對應座標。
  Automatically moves the mouse and clicks the matched location with `pyautogui`.
- **循環偵測**：以固定影格間隔重複偵測與點擊，達成無人值守自動遊玩。
  Repeats detection/clicking on a fixed frame interval for unattended play.

## 技術 / Tech Stack

Python、OpenCV (`cv2`)、NumPy、`pyautogui`

## 檔案結構 / File Overview

| 檔案 / File | 說明 / Description |
| --- | --- |
| `main.py` | 主程式：畫面擷取、模板比對、自動點擊 Main script: capture, match, click |
| `*.jpg` | 用於模板比對的按鈕/畫面截圖 Reference screenshots used as matching templates |

## 使用方式 / Usage

```bash
pip install opencv-python numpy pyautogui
python main.py
```

執行後程式會持續讀取攝影機/擷取畫面，偵測到對應按鈕即自動點擊，按下 `q` 結束程式。

Once running, the script continuously reads the video source, clicks matched buttons automatically, and exits when `q` is pressed.
