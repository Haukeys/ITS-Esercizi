#Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
# restituisca un nuovo dizionario con solo i prodotti che hanno un price inferiore a 50, ma
# con i prezzi aumentati del 10% e arrotondati a due cifre decimali.

def filtra_e_aumenta_prezzi(products:dict)->dict:
    products_higher:dict = {}
    for name, price in products.items():
        if price < 50:
            new_price = round(price * 1.10, 2)
            products_higher[name] = new_price
    return products_higher


price:dict={"pane":15, "acqua":150, "vino":35, "pizza":25, "gelato":158, "tonno":5, "pollo":80}

print(filtra_e_aumenta_prezzi(price))