#Import library
import cv2

#Import sub-program
import setup

#Use haarcascade function
haar_faces = cv2.CascadeClassifier(setup.HAAR_FACES)

#Detect single face on an image
def detect_single(image):
    """Return bounds (x, y, width, height) of detected face in grayscale image.
       If no face or more than one face are detected, None is returned.
    """
    faces = haar_faces.detectMultiScale(image, 
                scaleFactor=setup.HAAR_SCALE_FACTOR, 
                minNeighbors=setup.HAAR_MIN_NEIGHBORS, 
                minSize=setup.HAAR_MIN_SIZE, 
                flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) != 1:
        return None
    return faces[0]

#Crop the image based on the recognized face to fit the frame
def crop(image, x, y, w, h):
    crop_height = int((setup.FACE_HEIGHT / float(setup.FACE_WIDTH)) * w)
    midy = y + h/2
    y1 = int(max(0, midy-crop_height/2))
    y2 = int(min(image.shape[0]-1, midy+crop_height/2))
    return image[y1:y2, x:x+w]

#Resize a face image to the proper size for training and detection
def resize(image):
    return cv2.resize(image, 
                      (setup.FACE_WIDTH, setup.FACE_HEIGHT), 
                      interpolation=cv2.INTER_LANCZOS4)