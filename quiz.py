# Main program that runs the quiz

import os

if __name__ == "__main__":
    cwd = os.getcwd()
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

    print(symbolDict[symbolNames[0]])