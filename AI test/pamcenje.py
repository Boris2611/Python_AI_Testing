def Pamcenje(ulaz, izlaz, odgovor):
    
    memorijaFileName = "Memorija.txt"
    memorija = open(memorijaFileName, "a", encoding="utf8")

    memorija.write("\nUlaz: " + ulaz + "\n")
    memorija.write("Izlaz: " + izlaz + "\n")
    memorija.write("Odgovor: " + odgovor + "\n")
    
    memorija.close()
