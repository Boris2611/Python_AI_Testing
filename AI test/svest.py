import obrada_ulaza
import obrada_podataka
import obrada_izlaza
import pamcenje

#------ SVEST ----------

while True:
# Ulaz
    ulaz = input("Ulaz: ")

    
#----- PODSVEST -------

# Obrada Ulaza
    izlaz = obrada_ulaza.Obrada_ulaza(ulaz)
# Obrada Izlaza
    odgovor = obrada_izlaza.Obrada_izlaza(izlaz)


    ## Obrada Podataka
    odgovorNaPitanje = obrada_podataka.Obrada_podataka(ulaz, odgovor)
    print(odgovorNaPitanje)



    
# Pamcenje
    pamcenje.Pamcenje(ulaz, izlaz, odgovor)

