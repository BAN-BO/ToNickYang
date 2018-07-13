# 黑白图像存储，把每一帧都读出来
# 没有识别功能所以冗余度非常大
import numpy as np
import cv2
import os

output_dir = './demo_image'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture('NickYangDemo41s.mp4')
c = 1

index = 1
while (cap.isOpened()):
    print('[ INFO ] : Being processed picture %s' % index)
    ret, frame = cap.read()

    # 这里必须加上判断视频是否读取结束的判断,否则播放到最后一帧的时候出现问题了
    if ret is True:
        # Convert frame to grayscale  帧转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cv2.imshow('frame', gray)
    cv2.imwrite('demo_image/' + str(index) + '.jpg', frame)  # 存储为图像
    index = index + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
