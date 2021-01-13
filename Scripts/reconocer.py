#@author Anel Martínez
#Proyecto de Redes de Sensores
#Paralelo # 1
#Grupo #6
#Término 2019 1S
import cv2
import sys
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

from PIL import Image
import os, os.path
#Counters for emotions
cnt1=0
cnt2=0

#Function that predicts the facial expression of the faces in the directory
def clasificar():
    model = load_model("C:/Users/LENOVO/Desktop/camara/models/model_emotion.h5")#saved model path here)
    path = "C:/Users/LENOVO/Desktop/deteccion/caras" #faces images path
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        print(f)

    for it in files:
        test_image = image.load_img(it, target_size=(150, 150));
        test_image = image.img_to_array(test_image);
        test_image = np.expand_dims(test_image, axis=0);
        test_image = test_image.reshape(1, 150, 150, 3);

        result = model.predict_classes(test_image);
        if result==0:
            #cnt1+=1
            print("atento")
        else:
            #cnt2+=1
            print("aburrido")
        print(result)
    #return cnt1,cnt2


# Take a photo of the video capture of the webcam
def obtenerImagen():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')


    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Display
    cv2.imshow('img', img)
    img = cv2.imwrite('C:/Users/LENOVO/Desktop/deteccion/img.jpg', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(3000)

    # Release the VideoCapture object
    cap.release()

#Save all the images of faces from a photo
def sacarImagenes():
    img = 'C:/Users/LENOVO/Desktop/deteccion/img.jpg'
    img2 = cv2.imread(img)
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #Convert to gray scale

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = img2[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite('C:/Users/LENOVO/Desktop/deteccion/caras/'+str(w) + str(h) + '_faces.jpg', roi_color)#Save every face in the directory

    status = cv2.imwrite('faces_detected.jpg', img2)  #Save the global image
    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)


obtenerImagen();
sacarImagenes();
clasificar();