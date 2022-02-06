def Obrada_ulaza(ulaz):
  
    ulaz = ulaz.lower()
    
    if "?" in ulaz:
        ulaz = ulaz.replace("?","")
    elif "!" in ulaz:
        ulaz = ulaz.replace("!","")
    elif "." in ulaz:
        ulaz = ulaz.replace(".","")
    elif "," in ulaz:
        ulaz = ulaz.replace(",","")

    ulaz += ' '
    ulaznaRec = ''
    lista_ulaz = []
    for i in range(len(ulaz)):
        if ulaz[i] != " ":
            ulaznaRec += ulaz[i]
        else:
            lista_ulaz.append(ulaznaRec)
            ulaznaRec = ''

    ulaz_izlaz_file_name = "Ulaz_Izlaz.txt"
    ulaz_izlaz = open(ulaz_izlaz_file_name, "r+", encoding="utf8")

    ulazPozdrav = ulaz_izlaz.readline()
    ulazPitanje = ulaz_izlaz.readline()
    ulazUvreda = ulaz_izlaz.readline()
    ulazKompliment = ulaz_izlaz.readline()


    pozdrav = 0
    pitanje = 0
    uvreda = 0
    kompliment = 0

    idk = 0

    for i in range(len(lista_ulaz)):
        if lista_ulaz[i] in ulazPozdrav:
            pozdrav += 1

        elif lista_ulaz[i] in ulazPitanje:
            pitanje += 1

        elif lista_ulaz[i] in ulazUvreda:
            uvreda += 1

        elif lista_ulaz[i] in ulazKompliment:
            kompliment += 1

        else:
            idk += 1



    if uvreda > 0:
        izlaz = "Uvreda"
    elif kompliment > 0:
        izlaz = "Kompliment"
    elif (pitanje >= pozdrav and pitanje > uvreda and pitanje >= kompliment):
        izlaz = "Pitanje"
    elif (pozdrav > pitanje and pozdrav > uvreda and pozdrav >= kompliment):
        izlaz = "Pozdrav"
    else:
        izlaz = "Ne znam"
    
    return izlaz

    


    
