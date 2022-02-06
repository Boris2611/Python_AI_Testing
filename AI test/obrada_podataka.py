def Obrada_podataka(ulaz, odgovor):

    if "?" in ulaz:
        ulaz = ulaz.replace("?","")
    elif "!" in ulaz:
        ulaz = ulaz.replace("!","")
    elif "." in ulaz:
        ulaz = ulaz.replace(".","")
    elif "," in ulaz:
        ulaz = ulaz.replace(",","")

    pitanja_odgovori = open("Pitanja_Odgovori.txt", "r")
    pitanja = []
    odgovori = []

    while True:

        p = pitanja_odgovori.readline()
        if p == "":
            break
        if "\n" in p:
            p = p.replace("\n", "")
        pitanja.append(p)

        o = pitanja_odgovori.readline()
        if "\n" in o:
            o = o.replace("\n", "")
        odgovori.append(o)

            

      
        

    
    if odgovor == "PITANJE":
       for i in range(len(pitanja)):
            if ulaz == pitanja[i]:
               odgovor = odgovori[i]
        
    elif odgovor == "OSTALO":
        odgovor = "Ostalo"


    return odgovor
