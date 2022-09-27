#ChatBotBlock6
# -*- coding: utf-8 -*-
from csv import excel

s = 'Support-Bot'


#########################################################################################

#Start von den ChatBot
def ChatBotStart():
   
    options = ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Access', 'Visio']
    
    print(s + ": Willkommen, Ich bin " + s + ", bitte nennen Sie mir ein Produkt von Microsoft wo Sie Probleme haben.")
    print(s + ": Sollten Sie kein Problem haben, antworten Sie bitte mit: Nein")
    while True:
        global produkt
        produkt = input("")
        
        if produkt in options:
           WelchesProgramm()
#########################################################################################

#Auswahl des Programms
def WelchesProgramm():

    match produkt:

        case 'Word':
            WordAbfrage()

        case 'Excel':
            ExcelAbfrage()

        case 'PowerPoint':
            PowerPointAbfrage()

        case 'Outlook':
            OutlookAbfrage()

        case'Access':
            AccessAbfrage()

        case 'Visio':
            VisioAbfrage()

#########################################################################################

def WordAbfrage():
    wordoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Word genauer beschreiben?")
        
    while True:
        wordprodukt = input("")
        if wordprodukt in wordoptions:
            print(s + ": Hier sind die Lösungen")
            break
    input("Press ENTER to exit")
#########################################################################################

def ExcelAbfrage():
    exceloptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Excel genauer beschreiben?")

    while True:
        excelprodukt = input("")
        if excelprodukt in exceloptions:
            print(s + ": Hier sind die Lösungen")
            break
    input("Press ENTER to exit")
#########################################################################################

def PowerPointAbfrage():
    powerpointoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit PowerPoint genauer beschreiben?")

    while True:
        powerpointprodukt = input("")
        if powerpointprodukt in powerpointoptions:
            print(s + ": Hier sind die Lösungen")
            break
    input("Press ENTER to exit")
#########################################################################################

def OutlookAbfrage():
    outlookoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Outlook genauer beschreiben?")

    while True:
        outlookprodukt = input("")
        if outlookprodukt in outlookoptions:
            print(s + ": Hier sind die Lösungen")
            break
    input("Press ENTER to exit")
#########################################################################################

def AccessAbfrage():
    accessoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Access genauer beschreiben?")

    while True:
        accessprodukt = input("")
        if accessprodukt in accessoptions:
            print(s + ": Hier sind die Lösungen")
            break
    input("Press ENTER to exit")
#########################################################################################

def VisioAbfrage():
    visiooptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Visio genauer beschreiben?")

    while True:
        visioprodukt = input("")
        if visioprodukt in visiooptions:
             print(s + ": Hier sind die Lösungen")
             break
    input("Press ENTER to exit")
#########################################################################################


#Ausführen vom Programm

ChatBotStart()
