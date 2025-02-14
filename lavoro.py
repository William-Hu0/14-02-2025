inventario = {

0 : {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
1 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
2 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}
def menu():
    print(f"1. Aggiungere un prodotto nome, quantità e prezzo")
    print(f"2. Modificare la quantità di un prodotto esistente")
    print(f"3. Modificare il prezzo di un prodotto esistente")
    print(f"4. Eliminare un prodotto dall’inventario")
    print(f"5. Visualizzare l’intero inventario in modo leggibile")
    print(f"0. Per fermarti")
def add():
        nome=input("inserisci un nome")
        quantità=input("inserisci un quantità")
        prezzo=float(input("inserisci una prezzo"))
        inventario[idutente]={"nome": nome, "quantità": quantità, "prezzo":prezzo}
while True:
    menu()
    if y==1:
        idutente=int(input("inerisci l'id utente"))
        if idutente in inventario:
            print("c'è già")
        else:
            nome=input("inserisci un nome")
            quantità=input("inserisci un quantità")
            prezzo=float(input("inserisci una prezzo"))
            inventario[idutente]={"nome": nome, "quantità": quantità, "prezzo":prezzo}
    elif y==2:
        for chiave in inventario:
            print(f"{chiave} {inventario[chiave]}")
    elif y==3:
        idutente= int(input("quale indice vuoi modificare?"))
        a=input("caratteristica che vuoi cambiare")
        b=input("nuovo valore")
        inventario[idutente].update({a:b})
    elif y==4:
        idutente= input("quale indice vuoi modificare?")
        inventario.pop(idutente)
    elif y==7:
        print(len(inventario))
    elif y==8:
        del inventario
    elif y==0:
        break
    else:
        print("riprova")