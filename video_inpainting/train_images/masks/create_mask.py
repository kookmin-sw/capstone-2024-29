import cv2
import numpy as np
import random

for i in range(5440):
    width = 960
    height = 540

    mask = np.zeros((540, 960), dtype=np.uint8)

    num = random.randint(1, 3)
    for j in range(num):
        size = random.randint(100, 300)

        x = random.randint(0, width-size)
        y = random.randint(0, height-size)
        if j%2:
            cv2.rectangle(mask, (x,y), (x+size, y+size), (255), -1)
        else:
            cv2.circle(mask, (x+size//2, y+size//2), size//2, (255), -1)
    cv2.imwrite(f"./masks/{i}.png", mask)

cv2.destroyAllWindows()
