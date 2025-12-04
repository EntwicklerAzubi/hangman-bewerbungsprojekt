from os import system
from random import randint
from time import sleep

def clear_screen():
    try:
        system("cls")
    except:
        system("clear")
clear_screen() 

worte = [
    "abenteuer", "akrobat", "alchemie", "amphibie", "anemone", "archipel", "astronaut",
    "aurora", "ballade", "banane", "bibliothek", "blume", "boomerang",
    "brausetablette", "burg", "canyon", "chaos", "chrom", "delfin", "diamant", "diktator",
    "dinosaurier", "doktor", "drachen", "eclipse", "edelstein", "eleganz",
    "emigrant", "energie", "entdeckung", "epidemie", "esoterik", "explosion", "fabel",
    "fahrrad", "falke", "fantasie", "feuerwerk", "fossil", "fragile", "galaxie",
    "geheimnis", "genie", "geographie", "gewitter", "gletscher", "goblin",
    "gold", "granit", "grottenolm", "habitat", "hacker", "hagel", "halloween", "harmonie",
    "hase", "hedonist", "helium", "hibiskus", "himmel", "honig", "horizont", "hydraulik",
    "hyperion", "idee", "illusion", "impuls", "inspiration", "internet", "iris", "jagd",
    "jazz", "joghurt", "joker", "jubel", "jungle", "kabarett", "kaktus", "kamikaze",
    "karawane", "katakombe", "kakao", "kerze", "kibitze", "kinder", "kirschbaum", "klavier",
    "kleeblatt", "kobold", "komet", "konstruktion", "korn", "kraken", "kreuzfahrt", "krimi",
    "krypta", "kultur", "labyrinth", "lampe", "laser", "lavendel", "leben", "legende",
    "leopard", "licht", "lilie", "limousine", "lotus", "luchs", "magnet", "magie", "maler",
    "mandarine", "marathon", "marmor", "medaille", "melodie", "meteor", "mikroskop",
    "mineral", "mirage", "monolith", "mond", "monster", "muschel", "mythos",
    "narzisse", "nashorn", "nebula", "nektar", "netzwerk", "nymphe", "oase", "obsidian",
    "oktopus", "olymp", "opal", "orakel", "orchidee", "oxymoron", "panorama", "papagei",
    "paradies", "paradoxon", "pechvogel", "phantasie", "planet", "plasma",
    "polaris", "polka", "portal", "pyramide", "quintett", "quiz", "rakete",
    "rambazamba", "ranger", "regenbogen", "robot", "robust", "rose", "rubin", "rummel",
    "safari", "salz", "saphir", "satellit", "schach", "schatz", "scheune",
    "schmetterling", "schnecke", "schneesturm", "schwan", "sirene", "smaragd",
    "sommer", "spiegel", "spitze", "stern", "sturm", "sphinx", "talisman", "tampon", 
    "tornado", "trapez", "trommel", "tulpe", "turm", "universum",
    "vulkan", "walross", "wanderer", "wappen", "wasserfall", "webstuhl", "welle",
    "weltraum", "wolke", "zauber", "zeppelin", "zirkus", "zombie", "zyklus"
]

def main():

    hangman = [
    """
       _______
      |/      |
      |      
      |      
      |       
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      
      |       
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      (_)
      |       |
      |       |
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|
      |       |
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      / 
      |
    __|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      / \\
      |
    __|___
    """
    ]

    straf_punkte = 0 
    buchstaben = [] #die von spieler eingegebene Buchstaben
    wort = worte[randint(0, len(worte))] #zuffäliges Wort wird genommen aus unsere Liste WORTE

    while True:
        clear_screen()
        print("\n\n\n" + " " * 42 + " Hangman - Bewerbungsprojekt Pinic\n\n\n")
        print(hangman[straf_punkte]) # Zustand des Hangmans wird gezeigt jenachdem wie viel straf_punkten wir haben

        blank_count = 0
        print(" " * 54, end="", flush=True)

        for c in wort: #Ein Loop der die Anzahl von Buchstaben im Wort anzeigt. Falls wir die richtige Buchstabe schon haben wird die ersetzt
            if c in buchstaben:
                print(c + " ",end="", flush=True)
            else:
                print("_ ", end="", flush=True)
                blank_count += 1
        if(blank_count==0):
            break #heisst dass der spieler alle Buchstaben gesammelt hat, Loop hört auf und der Spieler kriegt eine Glückwunsch Nachricht

        guess = input("\n\n\n\n\nBuchstabe bitte raten : ")

        if len(guess) < 1 or len(guess) > 1: #Die maximale länge der Eingabe beträgt : 1
            print("Bitte nur eine Buchstabe einschreiben")
            sleep(1.5)
            continue
        
        try:
            x = int(guess) #hier wird sicher gestellt dass der Spieler keine Nummern in die Liste BUCHSTABEN speichern kann
            print("Bitte nur eine Buchstabe einschreiben")
            sleep(1.5)
            continue
        except:
            pass
        
        buchstaben += guess #Buchstabe wird nach überprüfung der Inhalt in die Buchstabenliste hinzugefügt

        if guess in wort: #hier wird überprüft ob das eingegebene Buchstabe im Wort zu finden ist
            pass
        else:
            straf_punkte += 1

        if straf_punkte == 7: #Spieler hat verloren
            clear_screen()
            print("\n\n\n" + " " * 42 + " Hangman - Bewerbungsprojekt Pinic\n\n\n")
            print(hangman[straf_punkte - 1])
            print("Du hast verloren! Keine Versuche mehr übrig - das Wort war [" + wort + "]")
            sleep(3)
            clear_screen
            exit()
    
    print("\n\nGlückwunsch, du hast das Wort entdeckt!!!") #Spieler hat gewonnen
    sleep(3)
    clear_screen()
    exit()

main()




