#Pi GPIO port which is connected to the LED indicator
LOCK_LEDRED_PIN = 17
LOCK_LEDGRN_PIN = 4

#Pi GPIO port which is connected to the relay solenoid door lock
DOOR_LOCK_PIN = 23

#Pi GPIO port which is connected to the camera's button
BUTTON_CAM_PIN = 24

#Pygame setup to call the audio files
import pygame

pygame.mixer.init()

WELCOME = pygame.mixer.Sound('your sound file directory(.ogg)')
TRYAGAIN = pygame.mixer.Sound('your sound file directory(.ogg)')
COMEBACK = pygame.mixer.Sound('your sound file directory(.ogg)')
NOFACE = pygame.mixer.Sound('your sound file directory(.ogg)')

#Threshold for the confidence of a recognized face before it's considered a
#positive match.  Confidence values below this threshold will be considered
#a positive match because the lower the confidence value, or distance, the
#more confident the algorithm is that the face was correctly detected.
#Start with a value of 3000, but you might need to tweak this value down if 
#you're getting too many false positives (incorrectly recognized faces), or up
#if too many false negatives (undetected faces).
POSITIVE_THRESHOLD = 4300.0

#File to save and load face recognizer model.
TRAINING_FILE = 'training.xml'

#Directories which contain the positive and negative training image data.
POSITIVE_DIR = './training/positive'
NEGATIVE_DIR = './training/negative'
CAPTURE_DIR = '/home/pi/Project/training/capture'

#Value for positive and negative labels passed to face recognition model.
#Can be any integer values, but must be unique from each other.
#You shouldn't have to change these values.
POSITIVE_LABEL = 1
NEGATIVE_LABEL = 2
CAPTURE_LABEL = 3

#Size (in pixels) to resize images for training and prediction.
#Don't change this
FACE_WIDTH  = 92
FACE_HEIGHT = 112

#Face detection cascade classifier configuration.
#Don't change the value
HAAR_FACES         = 'haarcascade_frontalface_alt.xml'
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

#Filename to use when saving the most recently captured image for debugging.
DEBUG_IMAGE = 'capture.pgm'

def get_camera():   
    #Camera to use for capturing images.
    #Use this code for capturing from the web camera:
    import webcam
    return webcam.OpenCVCapture()