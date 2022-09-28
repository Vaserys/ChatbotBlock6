#ChatBotBlock6
from csv import excel
import math

#########################################################################################

#Start von den ChatBot
def ChatBotStart():
   
    options = ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Access', 'Visio']
    
    print("Joe-Mama: Willkommen, Ich bin Joe-Mama, bitte nennen Sie mir ein Produkt von Microsoft, mit dem Sie Probleme haben.")
    print("Joe-Mama: Sollten Sie kein Problem haben, antworten Sie bitte mit: Nein")
    while True:
        produkt = input("")
        if produkt in options:
           break
#####################################################################################
#WORD-Abfrage

def WordAbfrage():
    wordoptions = ['Kaputt']
    print("Joe-Mama: Können Sie mir Ihr Problem mit Word genauer beschreiben?")
        
    while True:
        wordprodukt = input("")
        if wordprodukt in wordoptions:
            print("Joe-Mama: Hier sind die Lösungen")   
#######################################################################################

#Excel-Abfrage

def ExcelAbfrage():
    exceloptions = ['Kaputt']
    print("Joe-Mama: Können Sie mir Ihr Problem mit Excel genauer beschreiben?")

    while True:
        excelprodukt = input("")
        if excelprodukt in exceloptions:
            print("Joe-Mama: Hier sind die Lösungen")
#########################################################################################
#PowerPoint-Abfrage

def PowerPointAbfrage():
    powerpointoptions = ['Kaputt']
    print("Joe-Mama: Können Sie mir Ihr Problem mit PowerPoint genauer beschreiben?")

    while True:
        powerpointprodukt = input("")
        if powerpointprodukt in powerpointoptions:
            print("Joe-Mama: Hier sind die Lösungen")
#########################################################################################
# Outlook Abfrage

def OutlookAbfrage():
    outlookoptions = ['Kaputt']
    print("Joe-Mama: Können Sie mir Ihr Problem mit Outlook genauer beschreiben?")

    while True:
        outlookprodukt = input("")
        if outlookprodukt in outlookoptions:
            print("Joe-Mama: Hier sind die Lösungen")
#########################################################################################
#Access Abfrage

def AccessAbfrage():
    accessoptions = ['Kaputt']
    print("Joe-Mama: Können Sie mir Ihr Problem mit Access genauer beschreiben?")

    while True:
        accessprodukt = input("")
        if accessprodukt in accessoptions:
            print("Joe-Mama: Hier sind die Lösungen")
#########################################################################################
#Visio-Abfrage

def VisioAbfrage():
    visiooptions = ['Kaputt']
    print("Joe-Mama: Können Sie mir Ihr Problem mit Visio genauer beschreiben?")

    while True:
        visioprodukt = input("")
        if visioprodukt in visiooptions:
             print("Joe-Mama: Hier sind die Lösungen")
#########################################################################################


ChatBotStart()



input('Press ENTER to exit')