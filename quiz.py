# Main program that runs the quiz

import os
import tkinter as tk
import random

if __name__ == "__main__":
    # initial book keeping and iterables we'll need
    cwd = os.getcwd()
    random.seed()
    symbolNames = [
        'Ascendant Realm', 'Commune', 'Darkness', 'Drink', 'Earth', 'Enter', 'Fleet',
        'Black Garden', 'Give', 'Guardian', 'Black Heart', 'Hive', 'Kill', 'Light', 
        'Love', 'Pyramid', 'Remember', 'Savathun', 'Scorn', 'Stop', 'Tower', 'Traveler',
        'Witness', 'Worm', 'Worship'
    ]

    symbolDict = {
        'Ascendant Realm': 'ascend.jpg', 'Commune': 'commune.jpg', 'Darkness': 'darkness.jpg', 'Drink': 'drink.jpg',
        'Earth': 'earth.jpg', 'Enter': 'enter.jpg', 'Fleet': 'fleet.jpg', 'Black Garden': 'garden.jpg', 
        'Give': 'give.jpg', 'Guardian': 'guardian.jpg', 'Black Heart': 'heart.jpg', 'Hive': 'hive.jpg', 'Kill': 'kill.jpg', 
        'Light': 'light.jpg', 'Love': 'love.jpg', 'Pyramid': 'pyramid.jpg', 'Remember': 'remember.jpg', 
        'Savathun': 'savathun.jpg', 'Scorn': 'scorn.jpg', 'Stop': 'stop.jpg', 'Tower': 'tower.jpg', 'Traveler': 'traveler.jpg',
        'Witness': 'witness.jpg', 'Worm': 'worm.jpg', 'Worship': 'worship.jpg'
        }

    # initiate the tkinter window
    window = tk.Tk()
    
    # randomly choose an image to be quizzed
    correct = random.choice(symbolNames)

    # open the associated file and pack it into a frame


    # randomly choose the position of the 4 buttons with symbol names

    # determine if correct name was clicked, either loop with a new symbol or end the quiz

