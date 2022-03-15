# Main program that runs the quiz

import tkinter as tk
import random
from PIL import Image, ImageTk

# global vars
score = 0
buttons = []
correct = ''
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

if __name__ == "__main__":
    # create seed for random library
    random.seed()

    # initiate the tkinter window
    window = tk.Tk()
    window.title('Vow Symbol Quiz')
    frame = tk.Frame(window)

    # randomly choose 4 symbol names and the image to be shown
    def getSymbols():
        global buttons
        buttons = random.choices(symbolNames, k=4)

    def getCorrect():
        global correct
        correct = random.choice(buttons)

    
    # determine if correct name was clicked, either loop with a new symbol or end the quiz
    def check(button):
        global score
        if correct == buttons[button]:
            score += 1
            gameLoop()
        else:
            gameOver()
    
    # build the image for the main game screen
    def gameLoop():
        getSymbols()
        getCorrect()
        for widget in frame.winfo_children():
            widget.destroy()
        img = ImageTk.PhotoImage(Image.open(symbolDict[correct]))
        scoreLabel = tk.Label(frame, text=str(score))
        scoreLabel.pack()
        label = tk.Label(frame, image=img)
        label.pack()
        button0 = tk.Button(frame, text=buttons[0], command=lambda n=0: check(n))
        button0.pack()
        button1 = tk.Button(frame, text=buttons[1], command=lambda n=1: check(n))
        button1.pack()
        button2 = tk.Button(frame, text=buttons[2], command=lambda n=2: check(n))
        button2.pack()
        button3 = tk.Button(frame, text=buttons[3], command=lambda n=3: check(n))
        button3.pack()
        frame.pack()
        tk.mainloop()

    # build the game over screen
    def gameOver():
        for widget in frame.winfo_children():
            widget.destroy()
        label = tk.Label(frame, text='Game Over! Your final score was ' + str(score))
        label.pack()
        frame.pack()
        tk.mainloop()

    # begin the game
    gameLoop()
    

    

