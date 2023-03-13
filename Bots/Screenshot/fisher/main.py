from PIL import Image, ImageGrab
from threading import Thread

import numpy as np
import cv2 as cv
import time


class MainAgent: 
    # Self function
    def __init__(self) -> None:

        # Gets all agents
        self.agents = []

        # Creating variables
        self.fishing_thread = None

        #Captured Image
        self.currentimage = None        #BGR
        self.currentimagehsv = None     #HSV

        # More variables
        self.zone = 'feralas'
        self.time = 'night'

        print('Setup Complete')

# Screen capture function
def update_screen(agent):

    # Set current timeq
    t0 = time.time()

    while True: 
        # Capture the screen, and store it with the correct colour scaling
        agent.currentimage = ImageGrab.grab()
        agent.currentimage = np.array(agent.currentimage)
        agent.currentimage =  cv.cvtColor(agent.currentimage, cv.COLOR_RGB2BGR)
        agent.currentimageHSV = cv.cvtColor(agent.currentimage, cv.COLOR_BGR2HSV)

        # Show captured image
        cv.imshow('Computer Vision', agent.currentimage)

        # Break when q is pressed
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        # Amount of iterations per seconds (FPS)
        ex_time = time.time() - t0
        print("FPS: " + str(1 / (ex_time)))
        t0 = time.time()

# Function for getting user input
def print_menu():
    print('Enter a command:')
    print('\tS\tStart the main agent.')
    print('\tZ\tSet Zone')
    print('\tF\tStart the fishing agent')
    print('\tQ\tQuit')

# Run as main
if __name__ == "__main__":

    # Call the main agent
    main_agent = MainAgent()

    # Start the user input menu
    print_menu()
    while True: 

        # Get user input
        user_input = input()
        user_input = str.lower(user_input).strip()

        # Start main agent
        if user_input == 's':

            # Create the thread
            update_screen_thread = Thread(
            target = update_screen, 
            args = (main_agent,),
            name = 'update screen thread',
            daemon = True)

            # Start the thread
            update_screen_thread.start()
            print('Thread Started')

        # Set the zone
        if user_input == 'z':
            pass
        # Start the fishing agent
        if user_input == 'z':
            pass
        # Exit
        if user_input == 'q':
            break
        else: print_menu()