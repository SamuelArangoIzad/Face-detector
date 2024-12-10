import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np


def main():
    # START THE WINDOW OF tkinter
    root = tk.Tk()
    root.title("FACE DETECTION")
    root.geometry("640x480+200+100")  # Size and position initial
    root.resizable(False, False)  # Block maximize and redimension
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Block closing with X

    # Start the video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: CAMERA NOT FOUND")
        return

    # Load the HAAR-CASCADE face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    #Load the HAAR-CASCADE face detection classifier
    recognizer =cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('models/face_trainer.yml') #Charge the model


    # Label to display frames in tkinter
    label = tk.Label(root)
    label.pack()


    # Function to capture and update the frame
    def update_frame():
        ret, frame = cap.read()
        if not ret:
            print("ERROR: THE FRAME IS LOST")
            root.destroy()
            return

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw a rectangle around detected faces
        for (x, y, w, h) in faces:

            face = gray[y:y+h, x:x+w]

            #Recognize the face using the trained model
            id_, confidence = recognizer.predict(face)

            #IF THE CONFIDENCE IS BELOW A CERTAIN THRESHOLD, CONSIDER IT A MATCH
            if confidence < 100:
                name = f"Access Check: Person {id_}"
            else:
                name = "ACCESS BLOCKED"

            #Draw the rectangle and the name
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cv2.putText(frame, name, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        # Convert the frame for tkinter compatibility (BGR to RGB)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(img))

        # Update the label with the new frame
        label.configure(image=img)
        label.image = img

        # Continue updating the frame every 10ms
        root.after(10, update_frame)

    # Function to exit the program when 'q' is pressed
    def exit_program(event):
        root.destroy()
        cap.release()
        cv2.destroyAllWindows()

    root.bind('q', exit_program)  # Bind 'q' to exit

    # Start the frame update loop
    update_frame()
    root.mainloop()


if __name__ == "__main__":
    main()
