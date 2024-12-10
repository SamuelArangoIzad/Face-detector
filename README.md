# Face-detector
Este repositorio consta de un programa pequeño que me costo aproximadamente 7 meses en desarrollar dónde se desarrolla el aprendizaje por imagenes 
y el manejo de las librerias numpy, os, cv2 por medio del lenguaje python usando OpenCV y Tkinter para crear un sistema de 
detección y reconocimiento facial. Captura fotogramas de vídeo de una cámara web, detecta rostros en tiempo real mediante un clasificador en cascada Haar y reconoce rostros mediante un modelo LBPH (histogramas de patrones binarios locales) entrenado previamente.

## Características principales:
Detección de rostros en tiempo real: utiliza el clasificador en cascada Haar de OpenCV para detectar rostros en la señal de la cámara web.
Reconocimiento facial: entrena un modelo de reconocimiento facial con imágenes almacenadas en una carpeta de fotos y lo utiliza para el reconocimiento facial en tiempo real.

##GUI de Tkinter:
muestra un vídeo en directo con los rostros detectados y los resultados del reconocimiento en una GUI.
Control de acceso: muestra "Acceso concedido" o "Acceso denegado" en función del resultado del reconocimiento.


####El sistema se entrena con imágenes almacenadas en un directorio de fotos y el modelo entrenado se guarda como face_trainer.yml en la carpeta de modelos.
