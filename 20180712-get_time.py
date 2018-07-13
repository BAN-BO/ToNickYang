# 获取被识别人的特征信息
# 本代码获取100张后自动停止
# 只有面部图片，并且为灰度图像
# Import OpenCV2 for image processing
import cv2
import os


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


# Start capturing video
# vid_cam = cv2.VideoCapture(0)
vid_cam = cv2.VideoCapture('./NickYangDemo41s.avi')

# 分类器所在路径获取分类器
path_haarcascade_frontalface_default = "./tool/"
face_detector = cv2.CascadeClassifier(path_haarcascade_frontalface_default + "haarcascade_frontalface_default.xml")

# For each person, one face id
face_id = 1

# Initialize sample face image
count = 0

assure_path_exists("get_time_dataset/")

# Start looping
while (True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # 这里必须加上判断视频是否读取结束的判断,否则播放到最后一帧的时候出现问题了
    if _ is True:
        # Convert frame to grayscale  帧转换为灰度图
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x, y, w, h) in faces:
        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("get_time_dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    # 因为视频是10帧每秒，因此每一帧等待100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count > 100:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()

print("[ INFO ] : Release resources.")
