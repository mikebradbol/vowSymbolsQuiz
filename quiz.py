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
        'Ascendant Realm': 0, 'Commune': 0, 'Darkness': 0, 'Drink': 0, 'Earth': 0, 
        'Enter': 0, 'Fleet': 0, 'Black Garden': 0, 'Give': 0, 'Guardian': 0, 
        'Black Heart': 0, 'Hive': 0, 'Kill': 0, 'Light': 0, 'Love': 0, 'Pyramid': 0, 
        'Remember': 0, 'Savathun': 0, 'Scorn': 0, 'Stop': 0, 'Tower': 0, 'Traveler': 0,
        'Witness': 0, 'Worm': 0, 'Worship': 0
        }

    # initiate the tkinter window
    window = tk.Tk()
    
    # randomly choose an image to be quizzed
    correct = random.choice(symbolNames)

    # open the associated file and pack it into a frame
    

    # randomly choose the position of the 4 buttons with symbol names

    # determine if correct name was clicked, either loop with a new symbol or end the quiz

