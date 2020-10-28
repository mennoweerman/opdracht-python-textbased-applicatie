import time
def beginverhaal():
    print("                ")
    print("Fijn dat je er bent,\n"
          "Beleef het verhaal van een Nieuwkomer in Nederland, Yasser Alsalak.\n"
          "Door bepaalde keuzes te maken kom je in Nederland terecht en krijg je de status van vluchteling of loopt het verhaal anders af.")
    print("                ")

def verhaalstukje1():
    time.sleep(4)
    print("VOOR HET VLUCHTEN")
    print("                ")
    print("Ik ben Yasser Alsalak en woon in een mooi huis in Damascus, samen met mijn vrouw en vier kinderen genieten wij van het leven."
          "Ik heb een goedlopende kapperszaak en veel klanten  \n" "Tot die bewuste maandag in 2013. Wij waren eten bij mijn moeder.\n")
    print("                 ")
    print ("A. Bij mijn moeder")
    print ("B. De buurman belt\n")
    print("                ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje2()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje(1)
def verhaalstukje2():
    time.sleep(4)
    print("Mijn moeder woont een paar kilometer van ons huis vandaan.\n")
    print("A. Tijdens het eten kwamen er ineens een hoop vliegtuigen over.")
    print("B. Tien minuten later belde de buurman.\n")
    print("                  ")
    antwoord = input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje5()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje2()
def verhaalstukje3():
    time.sleep(4)
    print("Met de mededeling dat Yasser naar huis moet komen.\n")
    print("A. Yasser zei dat de buurman moest wachten omdat zij aan het eten waren.")
    print("B. Hij liet zijn vrouw en dochters bij zijn moeder achter en reed naar huis.\n")
    print("                  ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje4()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje5()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje3()
def verhaalstukje4():
    time.sleep(4)
    print("Maar de buurman drong aan, hij moest NU komen.\n")
    verhaalstukje5()
def verhaalstukje5():
    time.sleep(4)
    print("Overal liepen huilende mensen rond. Alle huizen waren met de grond gelijk gemaakt door de bombardementen, ook van het huis van Yasser en zijn kapperszaak was niet meer over.\n"
    "Alles was weg, ook zijn spaargeld wat in de woning lag was in vlammen opgegaan.\n")
    print("A. Hij keerde terug naar zijn moeder, naar zijn gezin.")
    print("B. Leven in Damascus was niet meer mogelijk")
    print("                ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        print("Als een wonder waren mijn kinderen en vrouw ongedeerd.")
        verhaalstukje6()
    elif antwoord=="B" or antwoord=="b":
        print("Wij leefde continu in angst, vluchten was de enige optie.....")
        verhaalstukje7()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje5()
def verhaalstukje6():
    time.sleep(4)
    print("                ")
    print("In Damascus werd geplunderd, geschoten en er werden zelfs kinderen gekidnapt.")
    print("Vijftien dagen lang hebben wij ondergedoken gezeten in een kelder, na deze traumatische ervaring beluit Yasser Syrië te ontvluchten.")
    print("                ")
    verhaalstukje7()
def verhaalstukje7():
    time.sleep(4)
    print("                 ")
    print("TIJDENS HET VLUCHTEN")
    print("                ")
    print("Yasser verkoopt zijn auto en met de opbrengst daarvan vertrekt hij met zijn vrouw en twee jonge dochters naar Algerije.")
    print("De reis verloopt alles behalve soepel en er breekt opnieuw een verschrikkelijke periode aan.")
    print("A. Drie dagen lang slaapt de familie Alsalak met 37 andere gezinnen op het vliegveld van Algerije.")
    print("B. €1200,= per persoon.")
    print("                ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        print("voordat zij de grens van Libië over worden gesmokkeld.")
        verhaalstukje8()
    elif antwoord=="B" or antwoord=="b":
        print("kosten het om de grens van Libië over te kunnen worden gesmokkeld.")
        print("Dit geld had Yasser bij elkaar gesprokkeld door zijn auto te verkopen en geld te lenen.")
        verhaalstukje8()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje7()
def verhaalstukje8():
    time.sleep(4)
    print("                ")
    print("Na nog twee dagen hutjemutje met alle gezinnen in een huis te hebben gezeten maken zij de overtocht naar Sicilië.")
    print("Met 380 man zaten zij 19 uur lang tegen elkaar aan en gehurkt in een boot. Zonder eten of drinken.")
    print("Omdat zijn dochters zo’n dorst hadden heeft Yasser zijn dochters kleine beetjes zeewater laten drinken.")
    print("                ")
    print("A. Boten sloegen om.")
    print("B. Het gezin overleeft wonder boven wonder de overtocht.")
    print("                  ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        print("Voor hun ogen sloegen twee boten om en zagen zij hoe mensen verdronken. De mannen wilde helpen maar mochten onder geen beding opstaan.")
        print("Yasser heeft de ogen van zijn dochters afgedekt.")
        print("Het gezin overleeft wonder boven wonder de overtocht. Toen zij helikopters van het Rode kruis zagen wisten zij dat ze veilig waren.Wat hebben zij gehuild!")
        verhaalstukje9()
    elif antwoord=="B" or antwoord=="b":
        print("Toen zij helikopters van het Rode kruis zagen wisten zij dat ze veilig waren.")
        print("Wat hebben zij gehuild!")
        print("Even later kwamen de Italianen en werden zij vervoerd naar hotels. Zij kregen schonen kleding, eten en drinken. Zij hadden het gered!")
        verhaalstukje9()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje8()
def verhaalstukje9():
    time.sleep(4)
    print("                ")
    print("IN NEDERLAND")
    print("                ")
    print("Inmiddels was Yasser zijn oudste zoon aangekomen in het asielzoekerscentrum (AZC) in Ter Apel.")
    print("Yasser wilde ook naar Nederland, en dat is gelukt.")
    print("                ")
    print("A. Wat waren zij blij toen zij op het Centraal Station in Amsterdam aankwamen.")
    print("B. Veel van AZC’s wisselen.")
    print("                ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        print("Omdat er veel vluchtelingen waren moesten zij veel van AZC’s wisselen.")
        print("Na in verschillende AZC’s te zijn ondergebracht kregen zij een huis in Abcoude.")
        verhaalstukje10()
    elif antwoord=="B" or antwoord=="b":
        print("Na in verschillende AZC’s te zijn ondergebracht kregen zij een huis.")
        print("Ze kregen een huis in Abcoude, er moest nog een hoop gebeuren.")
        verhaalstukje10()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje9()
def verhaalstukje10():
    time.sleep(4)
    print("                ")
    print("Het Huis.")
    print("                ")
    print("Er moest een hoop aan het huis gedaan worden maar vanaf dag één kreeg hij hulp van alle buren.")
    print("Na twintig dagen was het bewoonbaar en kon Yasser zijn gezin uit het AZC laten overkomen.")
    print("Ze wisten niet wat ze zagen, een nieuw vellig onderkomen.")
    print("                ")
    print("A. Tegenprestatie.")
    print("B. Binnen de kortste keren kende iedereen Yasser.")
    print("                ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                   ")
    if antwoord=="A" or antwoord=="a":
        print("Als tegenprestatie voor alle hulp die Yasser had gekregen in zijn woning knapte hij klusjes op voor abcoudenaren.")
        print("Deze klusjes waren erg divers, Yasser wilde iets terug doen...")
        verhaalstukje11()
    elif antwoord=="B" or antwoord=="b":
        print("zelf de lokale kapperszaak werd benaderd door dorpsbewoners of zijn geen barbier konden gebruiken.")
        verhaalstukje11()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje10()
def verhaalstukje11():
    time.sleep(4)
    print("                   ")
    print("Pop- up Project.")
    print("                ")
    print("In 2017 werd er in de voormalige supermarkt een pop-up project Proof gestart.")
    print("Daar kon Yasser als barbier aan de slag.")
    print("Na een tijdje stopte het pop-up project en sindsdien werkt Yasser in de kapperszaak Christiaan Coiffures als Barbier.")
    verhaalstukje12()
def verhaalstukje12():
    time.sleep(4)
    print("                ")
    print("DE TOEKOMST.")
    print("                ")
    print("Yasser ziet een verzekerde toekomst voor zichzelf en voor zijn kinderen.")
    print("Yasser en zijn gezin zijn helemaal gesetteld in Abcoude.")
    print("                ")
    print("A. Zijn kinderen.")
    print("B. Zijn moeder.")
    print("                ")
    antwoord= input("Maak een keuze, A of B? ")
    print("                   ")
    if antwoord=="A" or antwoord=="a":
        print("Zijn kinderen gaan naar school en spreken goed Nederlands.")
        print("Zij oudste zoon heeft inmiddels een eigen huis. De andere kinderen wonen nog thuis.")
        verhaalstukje13()
    elif antwoord=="B" or antwoord=="b":
        print("Zijn moeder is in Damascus gebleven en in 2018 Overleden.")
        print("Zijn vader was al voor het hele gebeuren overleden.")
        verhaalstukje13()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje12()
def verhaalstukje13():
    time.sleep(4)
    print("                ")
    print("Als het veilig in Damascus wordt, willen zij alleen op bezoek. Maar niet meer definitief terug. ")
    print("Nederlandse mensen, ze zijn heel aardig.")
    nogeenkeer()

 
def nogeenkeer():
    time.sleep(4)
    print("Hier eindigt het verhaal van Yasser. Wil je het nog eens beleven door misschien andere keuzes te maken?\n")
    print("A. Ja ik wil het nog eens doen, en terug naar het begin van het verhaal.")
    print("B. Nee ik wil stoppen.\n")
    antwoord = input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        print("                    ")
        print("                    ")
        print("                    ")
        verhaalstukje1()
    elif antwoord=="B" or antwoord=="b":
        exit()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        nogeenkeer()

beginverhaal()
verhaalstukje1()



