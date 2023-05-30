# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:04:20 2023

@author: simon
"""


# Funktion für die Auswahl des Notenschlüssels und Berechnung der Note
def result(notenschluessel, erreichtepunkte):

    if notenschluessel == 1:
        if erreichtepunkte_input >= 86:
            note = 1.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 82:
            note = 1.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 78:
            note = 1.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 74:
            note = 2.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 70:
            note = 2.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 66:
            note = 2.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 62:
            note = 3.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 58:
            note = 3.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 54:
            note = 3.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 50:
            note = 4.0
            bestanden = True
            return note, bestanden

        else:
            note = 5.0
            bestanden = False
            return note, bestanden
  
    elif notenschluessel == 2:
        if erreichtepunkte_input >= 95:
            note = 1.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 90:
            note = 1.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 85:
            note = 1.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 80:
            note = 2.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 75:
            note = 2.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 70:
            note = 2.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 65:
            note = 3.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 60:
            note = 3.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 55:
            note = 3.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 50:
            note = 4.0
            bestanden = True
            return note, bestanden

        else:
            note = 5.0
            bestanden = False
            return note, bestanden
        
    elif notenschluessel == 3:
        if erreichtepunkte_input >= 85:
            note = 1.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 80:
            note = 1.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 75:
            note = 1.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 70:
            note = 2.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 65:
            note = 2.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 60:
            note = 2.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 55:
            note = 3.0
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 50:
            note = 3.3
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 45:
            note = 3.7
            bestanden = True
            return note, bestanden

        elif erreichtepunkte_input >= 40:
            note = 4.0
            bestanden = True
            return note, bestanden

        else:
            note = 5.0
            bestanden = False
            return note, bestanden

# Variablendefinition
erreichtePunkte = []            
bestanden = []           
note = []
matrikelnummer = []
eingabe = "ja"

# Abfrage des zu verwendenden Notenschlüssels
notenschluessel = float(input("Welcher Notenschlüssel soll verwenden werden (1, 2 oder 3)?: "))


if notenschluessel not in [1, 2, 3]:
    # Abbruch des Programms, wenn keine gültige Eingabe
    print("Fehler: Ungültiger Notenschlüssel")

else:
    while eingabe == 'ja':
        # Eingabe der Matrikelnummer
        matrikelnummer_input = int(input("Matrikelnummer: "))
        
        # Hinzufügen an die Liste der Matrikelnummern
        matrikelnummer.extend([matrikelnummer_input])

        # Eingabe der erreichten Punkte
        erreichtepunkte_input = float(input("Erreichte Punkte: "))

        # Hinzufügen an die Liste mit den erreichten Punkten
        erreichtePunkte.extend([erreichtepunkte_input])

        # Berechnung der Note und ob bestanden mit Funktion result
        note_value, bestanden_value = result(notenschluessel, erreichtePunkte)

        # Hinzufügen an die Liste mit den Noten
        note.extend([note_value])

        # Hinzufügen an die Liste ob bestanden
        bestanden.extend([bestanden_value])
        
        # Ende der Eingabe, wenn nicht 'ja' eingegeben wird
        eingabe = str(input("Möchten Sie noch weiter Ergebnisse eintragen (ja / nein)?: "))
        
    # Tabellenausgabe der ersten Zeile Mtr., Punkte, Note, Bestanden
    print("\nMtr.","\t", end='')
    print("Punkte","\t", end='')
    print("Note","\t", end='')
    print("Bestanden","\t")
    
    # Werte ausgeben in Tabelle
    for index, x in enumerate(matrikelnummer):
        print(x,"\t", end='')
        print(erreichtePunkte[index],"\t", end='')
        print(note[index],"\t", end='')
        
        if bestanden[index] is True:
            print("ja")
        elif bestanden[index] is False:
            print("nein")
