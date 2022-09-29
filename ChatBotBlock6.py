#ChatBotBlock6
# -*- coding: utf-8 -*-

s = 'Support-Bot'
email = 'itsupport@mail.de'
rufnummer = '389345287954783'

#########################################################################################

#Start von den ChatBot
def ChatBotStart():
    options = ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Access', 'Visio']
    print(s + ": Willkömmen, Ich bin " + s + ", bitte nennen Sie mir ein Produkt von Microsoft wo Sie Probleme haben.")
    print(s + ": Sollten Sie kein Problem haben, antworten Sie bitte mit: Nein")
    while True:
        global produkt
        produkt = input()
        #produktliste = produkt.split()
        #print(produktliste)
        #vergleichen von List options und Liste produktliste
        #übereinstimmung abgleichen mit options
        #weitergabe options an WelchesProgramm

        if produkt in options:
           WelchesProgramm()
           break
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
#def ZusatzInfo():
#    print(s + "Email: " + email)
#    print(S + "Rufnummer: " + rufnummer)
#    input("Press Enter to Exit")

#########################################################################################

#Abfrage der Probleme bei Word
def WordAbfrage():
    wordoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Word genauer beschreiben?")

    while True:
        wordprodukt = input()
        if wordprodukt in wordoptions:
            print(s + ": Hier sind die Lösungen")
            print(s + "Sollten Sie weitere Fragen haben können Sie sich bei Folgenden Adressen melden:")
            print(s + "Email: " + email)
            print(s + "Rufnummer: " + rufnummer)
            break
    input("Press Enter to Exit")
#########################################################################################
#Abfrage der Probleme bei Excel
def ExcelAbfrage():
    exceloptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Excel genauer beschreiben?")

    while True:
        excelprodukt = input()
        if excelprodukt in exceloptions:
            print(s + ": Hier sind die Lösungen")
            print(s + "Sollten Sie weitere Fragen haben können Sie sich bei Folgenden Adressen melden:")
            print(s + "Email: " + email)
            print(s + "Rufnummer: " + rufnummer)
            break
    input("Press ENTER to exit")
#########################################################################################
#Abfrage der Probleme bei PowerPoint
def PowerPointAbfrage():
    powerpointoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit PowerPoint genauer beschreiben?")

    while True:
        powerpointprodukt = input()
        if powerpointprodukt in powerpointoptions:
            print(s + ": Hier sind die Lösungen")
            print(s + "Sollten Sie weitere Fragen haben können Sie sich bei Folgenden Adressen melden:")
            print(s + "Email: " + email)
            print(s + "Rufnummer: " + rufnummer)
            break
    input("Press ENTER to exit")
#########################################################################################
#Abfrage der Probleke bei Outlook
def OutlookAbfrage():
    outlookoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Outlook genauer beschreiben?")

    while True:
        outlookprodukt = input()
        if outlookprodukt in outlookoptions:
            print(s + ": Hier sind die Lösungen")
            print(s + "Sollten Sie weitere Fragen haben können Sie sich bei Folgenden Adressen melden:")
            print(s + "Email: " + email)
            print(s + "Rufnummer: " + rufnummer)
            break
    input("Press ENTER to exit")
#########################################################################################
#Abfrage der Probleme bei Access
def AccessAbfrage():
    accessoptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Access genauer beschreiben?")

    while True:
        accessprodukt = input()
        if accessprodukt in accessoptions:
            print(s + ": Hier sind die Lösungen")
            print(s + "Sollten Sie weitere Fragen haben können Sie sich bei Folgenden Adressen melden:")
            print(s + "Email: " + email)
            print(s + "Rufnummer: " + rufnummer)
            break
    input("Press ENTER to exit")
#########################################################################################
#Abfrage der Probleme bei Visio
def VisioAbfrage():
    visiooptions = ['Kaputt']
    print(s + ": Können Sie mir Ihr Problem mit Visio genauer beschreiben?")

    while True:
        visioprodukt = input()
        if visioprodukt in visiooptions:
             print(s + ": Hier sind die Lösungen")
             print(s + "Sollten Sie weitere Fragen haben können Sie sich bei Folgenden Adressen melden:")
             print(s + "Email: " + email)
             print(s + "Rufnummer: " + rufnummer)
             break
    input("Press ENTER to exit")
#########################################################################################


#Ausführen vom Programm

ChatBotStart()
