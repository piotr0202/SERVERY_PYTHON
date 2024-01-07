class Product:
    def __init__(self,name : str, price : float):
        #sprawdzam czy jest dluzsze niz 2 i czy ma odpowiednia strukture parametr name
        # czyli czy ma na poczatku przynajmniej jedna litere i czy ma potem przynajmniej
        #jedna cyfre
        czy_jest_litera = False
        czy_jest_liczba = False
        for i in name:
            if i.isalpha():
                czy_jest_litera = True
            if i.isdigit() and czy_jest_litera == 1:
                czy_jest_liczba = True
# Czy_jest_liczba implikuje fakt ze jest litera wczesniej ze wzgledu na warunki wiec mozna
# dokonac inicjalizacji pol klasy
        if (len(name) >= 2) and czy_jest_liczba:
            self.name = name
            self.price = price
        else:
            raise ValueError('Wrong product name, please enter a different product name.')

#nadpisanie metody klasowej __eq__ w taki sposób aby porównywać oba pola klasy
    def __eq__(self, other):
        if (self.name == other.name) and (self.price == other.price):
            return True
        else:
            return False

#nadpisanie metody klasowej __hash__ aby pokazywac oba parametry
    def __hash__(self) -> int:
        return hash(self.name, self.price)

# WŁASNE SPRAWDZENIE!
produkt = Product('butelka5',5.0)
print(produkt.name)
print(produkt.price)
produkt2 = Product('puszka_piwa1',4.0)
print(produkt.__eq__(produkt2))