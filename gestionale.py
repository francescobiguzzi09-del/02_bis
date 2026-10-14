aereo1 = {
    "codice": "ab-1",
    "modello": "A1",
    "ore_volo": 500,
    "controlli_ok": True
}
aereo2 = {
    "codice": "ab-2",
    "modello": "A2",
    "ore_volo": 523,
    "controlli_ok": True
}
aereo3 = {
    "codice": "ab-3",
    "modello": "B1",
    "ore_volo": 700,
    "controlli_ok": True
}
aereo4 = {
    "codice": "ab-4",
    "modello": "B2",
    "ore_volo": 575,
    "controlli_ok": False
}

aerei = []
aerei.append(aereo1)
aerei.append(aereo2)
aerei.append(aereo3)
aerei.append(aereo4)



def filtra_controlli_non_validi(aeromobili) -> list:
    return [aereo for aereo in aeromobili if aereo['controlli_ok'] == False]

def filtra_oltre_soglia(aeromobili, limite) -> list:
    return [aereo for aereo in aeromobili if aereo['ore_volo'] > limite]

def stampa_riepilogo(aeromobili):
    if not aeromobili:
        print("La lista è vuota! Nessun dato da stampare.")
        return
    for aereo in aeromobili:
        print(f"Codice: {aereo['codice']}, Modello: {aereo['modello']}, Ore volo: {aereo['ore_volo']}, Controlli: {'yes' if aereo['controlli_ok'] else 'no'}")

if __name__ == "__main__":
    limite_ore = 800
    print("LISTA DEGLI AEROMOBILI: ")
    stampa_riepilogo(aerei)
    print()
    print("LISTA DEGLI AEROMOBILI SENZA CONTROLLI: ")
    stampa_riepilogo(filtra_controlli_non_validi(aerei))
    print()
    print("LISTA DEGLI AEROMOBILI CHE SUPERANO IL LIMITE: ")
    stampa_riepilogo(filtra_oltre_soglia(aerei, limite_ore))
    




