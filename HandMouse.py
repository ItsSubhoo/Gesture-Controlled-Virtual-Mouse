import cv2
import mediapipe as mp
import time
import numpy as np
import math
import pyautogui as pyato
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
volume.GetMasterVolumeLevel()
maxvol = volume.GetVolumeRange()[0]
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
screen_weidth, screen_hight = pyato.size()

frangex = 100
frangey = 100
pMouse_x = 0
pMouse_y = 0
cMouse_x = 0
cMouse_y = 0
smoothinig = 2


# volume.SetMasterVolumeLevel(-20.0, None)


pTime = 0
x1 = y1 = x2 = y2 = 0
mphands = mp.solutions.hands
hands = mphands.Hands(min_detection_confidence=.7, max_num_hands=1)
mpDrow = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    reasults = hands.process(imgRgb)
    # print(reasults.multi_hand_landmarks)
    if reasults.multi_hand_landmarks:
        for onehand in reasults.multi_hand_landmarks:
            listnode = []
            openedF = 0

            cv2.rectangle(img, (frangex, frangey),
                          (width-frangex, height-frangey), (255, 0, 255), 3)
            for idno, lm in enumerate(onehand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                listnode.append([idno, cx, cy])

            x1 = y1 = x2 = y2 = 0
            caredfinger = [8, 12]
            indexup = 0
            midup = 0
            if (listnode[8][2] < listnode[6][2]):
                # print("index UP==",listnode[8][1])
                indexup = 1

                # print("index pos0","  not found","index pos1",listnode[8][1],"index pos2",listnode[8][2],"index pos3",listnode[8][3])
            if (listnode[12][2] < listnode[10][2]):
                # print("mid UP==",[12][2])
                mx, my = listnode[12][1], listnode[12][2]
                cv2.circle(img, (mx, my), 8, (0, 255, 0), cv2.FILLED)
                midup = 1

            if (indexup == 1 and midup == 1):
                print("both are up")
                x1 = listnode[8][1]
                y1 = listnode[8][2]

                x2 = listnode[12][1]
                y2 = listnode[12][2]
                cv2.circle(img, (x1, y1), 8, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 8, (0, 255, 0), cv2.FILLED)
                distance = math.hypot(x1-x2, y1-y2)
                print("distance=", distance)
                midx, midy = (x1+x2)//2, (y1+y2)//2
                if (distance < 32):

                    cv2.circle(img, (midx, midy), 18, (0, 0, 255), cv2.FILLED)
                    pyato.click()
                    pyato.sleep(.2)
                    print("clicked")
                # cv2.line(img, (x2, y2), (x1, y1), (0, 250, 0), 3)

            elif (indexup == 1 and midup == 0):
                mx, my = listnode[8][1], listnode[8][2]
                cv2.circle(img, (mx, my), 8, (0, 255, 0), cv2.FILLED)
                # index_x=screen_weidth/width*mx
                # index_y=screen_hight/height*my

                index_x = np.interp(
                    mx, (100, width-frangex), (0, screen_weidth))
                index_y = np.interp(
                    my, (100, height-frangey), (0, screen_hight))

                cMouse_x = pMouse_x+(index_x-pMouse_x)/smoothinig
                cMouse_y = pMouse_y+(index_y-pMouse_y)/smoothinig

                pyato.moveTo((screen_weidth - cMouse_x), cMouse_y)

                pMouse_x = cMouse_x
                pMouse_y = cMouse_y


                print("index up 0nly")
            elif (midup == 1 and indexup == 0):

                print("mid up only")

            distance = math.hypot()

            for i in range(0, 2):
                if (listnode[caredfinger[i]][2] < listnode[caredfinger[i]-2][2]):
                    openedF = openedF+1

            cv2.putText(img, "Finger Count"+str(int(openedF)), (10, 70),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 2)

            # mpDrow.draw_landmarks(img, onehand, mphands.HAND_CONNECTIONS)

            # mpDrow.draw_landmarks(img, onehand, mphands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.imshow("image", img)
    cv2.waitKey(1)
