import pyautogui
import findImg as fim
import math
import clientBounds as cb

def findClientBounds():
    topLeft = fim.getImgCoords('clientTopLeft')
    bottomRight = fim.getImgCoords('clientBottomRight')
    bottomLeft = [bottomRight[1],topLeft[0]]
    topRight  = [bottomRight[0],topLeft[1]]

    centerX = (bottomRight[0]+bottomLeft[0])/2
    centerY = (topRight[1]+bottomRight[1])/2

    # pyautogui.moveTo(centerX,centerY)

    clientBounds = {
        "topLeft":topLeft,
        "bottomRight":bottomRight,
        "bottomLeft":bottomLeft,
        "topRight":topRight,
        "centerX":centerX,
        "centerY":centerY
    }
    cb.clientBounds = clientBounds
    return clientBounds

# findClientBounds()