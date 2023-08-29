def convertir_12h_en_24h(heure_12h):
    heure_minute, periode = heure_12h.split()
    heure, minute = heure_minute.split(':')
    periode = periode.strip().upper()
    heure = int(heure)
    
    if periode == "PM" and heure != 12:
        heure = (heure + 12) % 24
    
    return f"{heure:02}:{minute}"

heure_12h = input("Entrez l'heure au format 12h (HH:MM AM/PM) : ")
heure_24h_convertie = convertir_12h_en_24h(heure_12h)
print(f"L'heure au format 24h est : {heure_24h_convertie}")
