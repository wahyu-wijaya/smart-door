#Import library
from gpiozero import LED, Button, Servo, OutputDevice

#Import sub-program
import setup

#Relay setup pin for the solenoid to work
door_lock = OutputDevice(setup.DOOR_LOCK_PIN, active_high=False, initial_value=False)

#Button setup pin
unlock = Button(setup.BUTTON_CAM_PIN,pull_up=True)

led_red = LED(setup.LOCK_LEDRED_PIN)
led_grn = LED(setup.LOCK_LEDGRN_PIN)