def convertir_24h_en_12h(heure_24h):
    heure, minute = map(int, heure_24h.split(':'))
    
    if heure < 0 or heure > 23 or minute < 0 or minute > 59:
        return "Format d'heure invalide."
    
    periode = "AM"
    if heure >= 12:
        periode = "PM"
    
    if heure == 0 or heure == 12:
        heure_12h = 12
    else:
        heure_12h = heure % 12
    
    return f"{heure_12h:02}:{minute:02} {periode}"

heure_24h = input("Entrez l'heure au format 24h (HH:MM) : ")
heure_12h_convertie = convertir_24h_en_12h(heure_24h)
print(f"L'heure au format 12h est : {heure_12h_convertie}")