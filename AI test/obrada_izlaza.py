import random

def Obrada_izlaza(izlaz):
    x = random.randint(0,2)

    listaPozdrava = ["Hej", "Pozdrav", "Ćao"]
    listaUvreda = ["Smrdljivko...", "Takođe", "F@#k"]
    listaPohvala = ["Hvala", "Hvalaa tii", "<3"]

    
    if izlaz == "Pozdrav":
        odgovor = listaPozdrava[x]
    elif izlaz == "Uvreda":
        odgovor = listaUvreda[x]
    elif izlaz == "Kompliment":
        odgovor = listaPohvala[x]
    elif izlaz == "Ne znam":
        odgovor = "OSTALO"
    else:
        odgovor = "PITANJE"

    return odgovor
