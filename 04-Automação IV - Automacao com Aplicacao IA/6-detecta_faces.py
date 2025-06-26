import cv2 # pip install opencv-python  // uma das principais bibliotecas para trabalhar com processamento de imagem
import dlib # precisa ser instalado de acordo com a versao do python, https://github.com/Murtaza-Saeed/dlib
import numpy as np

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
print(detector)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_img)
    
    # print(faces)
    i = 0
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(
            frame,
            (x, y),
            (x1, y1),
            (0, 255, 0),
            2
        )
        i += 1
        cv2.putText(
            frame,
            'Qtd face '+str(i),
            (x-10, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )
        print(face, i)
    
    cv2.imshow("Detecção Facial", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
