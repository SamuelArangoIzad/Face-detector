import cv2
import os
import numpy as np

#Rute of the archive with the images
photos_folder = '../Photos'
photos_list = os.listdir(photos_folder)


#==================================================================//

# Verifica si la carpeta existe
if not os.path.exists(photos_folder):
    print(f"Error: La carpeta '{photos_folder}' no existe.")
else:
    # Itera a través de los archivos de la carpeta 'Photos'
    for filename in os.listdir(photos_folder):
        # Verifica si el archivo tiene extensión .jpg o .png
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(f"Archivo válido encontrado: {filename}")


#==================================================================//


#Charge the clasification Haar Cascade for detection of the faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Create the model LBPH for recognition face
recognizer = cv2.face.LBPHFaceRecognizer_create()

#OKEY for saved the faces and the IDs associate
faces = []
ids = []

#Reload the images of the archive photos and ticket
for filename in os.listdir(photos_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(photos_folder, filename)
        image = cv2.imread(image_path)

        #Transform the image to color gray
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #Detecting the faces in the image
        detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for(x, y,w,h) in detected_faces:
            face = gray[y:y+h, x:x+w]
            faces.append(face)

            #THE ID OF THE PEOPLE IN THE ARCHIVE WITH OUT THE EXTENTION
            id = int(filename.split('.')[0].replace("persona", ""))
            ids.append(id)

#Login in the model with the faces detected
recognizer.train(faces, np.array(ids))

#Saved the model
recognizer.save('../models/face_trainer.yml')

print("MODEL OF RECOGNITION FATIAL SAVED")