# Main program that runs the quiz

import os
import tkinter as tk
import random
from PIL import Image, ImageTk

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

    def check(button):
        if correct == buttons[button]:
            print('correct')
        else:
            print('wrong')

    # initiate the tkinter window
    window = tk.Tk()
    window.title('Vow Symbol Quiz')
    
    # randomly choose the four names for the buttons and which of them will be the symbol shown
    buttons = random.choices(symbolNames, k=4)
    correct = random.choice(buttons)

    # open the associated file and pack it into a frame
    img = ImageTk.PhotoImage(Image.open(symbolDict[correct]))
    label = tk.Label(window, image=img)
    label.pack()
    button0 = tk.Button(text=buttons[0], command=lambda n=0: check(n))
    button0.pack()
    button1 = tk.Button(text=buttons[1], command=lambda n=1: check(n))
    button1.pack()
    button2 = tk.Button(text=buttons[2], command=lambda n=2: check(n))
    button2.pack()
    button3 = tk.Button(text=buttons[3], command=lambda n=3: check(n))
    button3.pack()
    tk.mainloop()

    # determine if correct name was clicked, either loop with a new symbol or end the quiz

