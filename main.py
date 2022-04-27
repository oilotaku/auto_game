import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(1)


def chack_icon( img, icon, lr):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    icon_h, icon_w = icon.shape[:2]
    res = cv2.matchTemplate(img_gray, icon, cv2.TM_CCOEFF_NORMED)
    threshold = lr
    # 取匹配程度大于 80% 的坐标
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # *表示可选参数
        return pt, (pt[0] + icon_w, pt[1] + icon_h), (pt[0] + 0.5 * icon_w, pt[1] + 0.5 * icon_h)


def click_icon( img, icon, lr=0.8, time_=0):
    try:
        x, y = pyautogui.position()
        pt, pt_wh, pt_point = chack_icon(img, icon, lr)
        cv2.rectangle(img, pt, pt_wh, (0, 0, 255), 2)
        print(pt_point)
        # pyautogui.moveTo(pt_point[0] * 1.5, pt_point[1] * 1.5, time_)
        pyautogui.click(x=pt_point[0] * 1.5, y=pt_point[1] * 1.5)
        pyautogui.moveTo(x, y)
        # click_icon(chack_icon(img, start_game_play_img)[2][0],chack_icon(img, start_game_play_img)[2][1][0],chack_icon(img, start_game_play_img)[2][0],chack_icon(img, start_game_play_img)[2][1][1])
    except:
        pass

if __name__ == '__main__':
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 60)
    start_game_play_img = cv2.imread('./start_game_play.jpg', 0)
    start_game_play_2_img = cv2.imread('./start_game_play_2.jpg', 0)
    end_game_img = cv2.imread('./end_game.jpg', 0)
    butten_X_img = cv2.imread('./butten_X.jpg', 0)
    i = 0
    while cap.isOpened():
        _, img = cap.read()
        i = i+1
        if i == 120:
            i = 0
            click_icon(img, start_game_play_img, lr=0.6)

            click_icon(img, start_game_play_2_img)

            click_icon(img, end_game_img)

            click_icon(img, end_game_img)

            click_icon(img, butten_X_img)

        cv2.imshow('img', img)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('./text.jpg', img)
            break
cv2.destroyAllWindows()
