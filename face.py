import cv2
import numpy as np

filename = 'D:/haarcascade_frontalface_default.xml'
detechtor = cv2.CascadeClassifier(filename)

recog = cv2.face.LBPHFaceRecognizer_create()
faces = []
ids = []  # 記錄該人臉id 的串列

# 注意圖片張數
for i in range(1, 20):
    # img = cv2.imread(f'face01/{1}.jpg')            #依序開啟每一張某英文的照片
    filename = f'D:/PythonCode/Opencv/face01/(1).jpg'
    print(filename)
    img = cv2.imread(filename)                      # 依序開啟每一張某英文的照片

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 色彩轉換成黑白
    img_np = np.array(gray, 'uint8')                # 轉換成指定編碼的 numpy 陳列
    face = detector.detectMultiScale(gray)          # 攝取人臉區域
    for (x, y, w, h) in face:
        faces.append(img_np[y:y+h, x:x+w])            # 記錄蔡英文人臉的位置和大小內像素的數值
        ids.append(1)                               # 記錄蔡英文人臉對應的id,只能是整數,卻是1表


# 注意圖片張數
for i in range(1, 10):
    # ing- cv2.imread(f*face02/(1).jpg')
    filename = f'D:/PythonCode/Opencv/face02/{1}.jpg'  # 依序開數每一張川普的照片
    print(filename)
    img = cv2.imread(filename)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_np = np.array(gray, 'uint8')                 # 轉換成指定編碼的 numpy 陳列
    face = detector.detectMultiScale(gray)           # 攝取人臉區域
    for (x, y, w, h) in face:
        faces.append(img_np[y:y+h, x:x+w])             # 記錄禁英文人臉的位置和大小內像素的數值
        ids.append(1)

print('training...')                    # 提示開始訓練
recog.train(faces, np.array(ids))       # 開始訓練
recog.save('face.yml')                  # 訂訓練完成儲存為 face.yml
print('ok!')
