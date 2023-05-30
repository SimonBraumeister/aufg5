# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:04:20 2023

@author: simon
"""



def result(notenschluessel, erreichtepunkte):

    if notenschluessel == 1:
        if erreichtepunkte_input >= 86:
            note = 1.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 82:
            note = 1.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 78:
            note = 1.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 74:
            note = 2.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 70:
            note = 2.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 66:
            note = 2.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 62:
            note = 3.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 58:
            note = 3.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 54:
            note = 3.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 50:
            note = 4.0
            bestanden = "ja"
            return note, bestanden

        else:
            note = 5.0
            bestanden = "nein"
            return note, bestanden
  
    elif notenschluessel == 2:
        if erreichtepunkte_input >= 95:
            note = 1.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 90:
            note = 1.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 85:
            note = 1.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 80:
            note = 2.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 75:
            note = 2.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 70:
            note = 2.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 65:
            note = 3.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 60:
            note = 3.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 55:
            note = 3.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 50:
            note = 4.0
            bestanden = "ja"
            return note, bestanden

        else:
            note = 5.0
            bestanden = "nein"
            return note, bestanden
        
    elif notenschluessel == 3:
        if erreichtepunkte_input >= 85:
            note = 1.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 80:
            note = 1.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 75:
            note = 1.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 70:
            note = 2.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 65:
            note = 2.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 60:
            note = 2.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 55:
            note = 3.0
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 50:
            note = 3.3
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 45:
            note = 3.7
            bestanden = "ja"
            return note, bestanden

        elif erreichtepunkte_input >= 40:
            note = 4.0
            bestanden = "ja"
            return note, bestanden

        else:
            note = 5.0
            bestanden = "nein"
            return note, bestanden

erreichtepunkte = []            

bestanden = []           

note_keys = [1, 2, 3]

note = []

matrikelnummer = []

notenschluessel = float(input("Welcher Notenschlüssel soll verwenden werden (1, 2 oder 3)?: "))

eingabe = "ja"

if notenschluessel not in [1, 2, 3]:

    print("Fehler: Unbekannter Notenschlüssel")

else:

    while eingabe == 'ja':

        matrikelnummer_input = int(input("Matrikelnummer: "))

        matrikelnummer.extend([matrikelnummer_input])

        erreichtepunkte_input = float(input("Erreichte Punkte: "))

        erreichtepunkte.extend([erreichtepunkte_input])

        note_value, y = result(notenschluessel, erreichtepunkte)

        note.extend([note_value])

        bestanden.extend([y])

        eingabe = str(input("Möchten Sie noch weiter Ergebnisse eintragen (ja / nein)?: "))

    print("\nMtr.","\t", end='')

    print("Punkte","\t", end='')

    print("Note","\t", end='')

    print("Bestanden","\t")

 

    a = 0

    b = 0

    c = 0

    for x in matrikelnummer:

        print(x,"\t", end='        ')

        print(erreichtepunkte[a],"\t", end='            ')

        print(note[b],"\t", end='')

        print(bestanden[c])

        a = a + 1

        b = b + 1

        c = c + 1
