import cv2
import downloader
import colorsys, os, sys
from PIL import Image, ImageDraw


def face(image):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread(image)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 
    if type(faces) is tuple:
        return False
    else:
        return True






