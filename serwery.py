from Product import Product
from abc import ABC,abstractmethod
from typing import Dict, List, Optional
from my_exception import listTooLong

#klasa serwer dziedziczaca po ABC gdyz jest to klasa abstrakcyjna
class Server(ABC):
#atrybut klasowy a nie instancji określający max długośc listy produktów
#zwracanej przez metody dla danego typu serwera, -> metody .get_entries()
    n_max_returned_entries = 3
    def __init__(self,*args,**kwargs):
        super().__init__()
#zadeklarowanie metody abstrakcyjnej bez definicji
    @abstractmethod
    def get_entries(self,n_letters : int = 1) -> List[Product]:
        pass


# Stworzenie klasy MapServer dziedziczacej po abstrakcyjnej klasie Server
# dostająca jako parametr słownik nazwy produktu i produktu.
class MapServer(Server):
    def __init__(self,strProd : Dict[str,Product],*args,**kwargs):
        self.__products = strProd
        super().__init__(*args,**kwargs)

#stworzenie listy produktów niedłuższej niż parametr klasowy n_max_returned_entries

    def get_entries(self, n_letters : int = 1) -> List[Product]:
        lista = []
        #iteruje po kluczach i wartościach w słowniku
        for keys,values in self.__products.items():
            czy_okej = True
            for i in range(n_letters):
                #jeśli pierwsze n_letters elementów string'a nie jest literami to nie zwracaj
                if not (keys[i]).isalpha():
                    czy_okej = False
            #jeśli nie ma 2 lub 3 cyfr na końcu nazwy to nie zwracaj
            if ((len(keys) - n_letters) > 1) and ((len(keys) - n_letters < 4)):
                #sprawdź czy ostatnie 2/3 elementy to cyfry, jeśli nie to nie zwracaj
                for i in range(len(keys) - n_letters):
                    if not (keys[n_letters + i]).isdigit():
                        czy_okej = False
            #jeśli wszystko ok powyżej to zwracaj
            if czy_okej:
                lista.append(values)
                #ostatnie sprawdzenie czy lista jest którsza niż parametr klasowy n_max_returned_entries
                if len(lista) > self.n_max_returned_entries:
                    #jeśli nie to wyrzuć wyjątek !
                    raise listTooLong('Number of found products exceeds its maximum number')
        return lista
#SPRAWDZENIE MOJE!
butelka = Product('bottle23',5.0)
serw = MapServer({'bottle23' : butelka})
print(serw.get_entries(6)[0].name)

#klasa analogiczna jak MapServer tylko zamiast słownika mamy listę
#jeśli coś niezrozumiałe to przeanalizujcie poprzednią klasę
class ListServer(Server):
    def __init__(self, strProd : List[Product],*args,**kwargs):
        self.__products = strProd
        super().__init__(*args,**kwargs)

    def get_entries(self,n_letters : int = 1) -> List[Product]:
        lista = []
        for prod in self.__products:
            czy_okej = True
            for i in range(n_letters):
                if not (prod.name[i]).isalpha():
                    czy_okej = False
            if ((len(prod.name) - n_letters) > 1) and ((len(prod.name) - n_letters < 4)):
                for i in range(len(prod.name) - n_letters):
                    if not (prod.name[n_letters + i]).isdigit():
                        czy_okej = False
            if czy_okej:
                lista.append(prod)
                if len(lista) > self.n_max_returned_entries:
                    raise listTooLong('Number of found products exceeds its maximum number')
        return lista

#SPRAWDZENIE MOJE!
produkt = Product('butelk51',5.0)
produkt2 = Product('butelk21',5.0)
produkt3 = Product('butelk31',5.0)
produkt4 = Product('butelk41',5.0)
serw = ListServer([produkt,produkt2,produkt3])
print(serw.n_max_returned_entries)
print(serw.get_entries(6))

#klasa Client, która ma dostawać jako parametr Server
class Client:
    def __init__(self,server : Server):
        self.server = server
#metoda która oblicza sumę cen produktów znajdujących się na liście zwróconej przez
# metodę server.get_entries()
    def get_total_price(self, n_letters : Optional[int]) -> Optional[float]:
        try:
            lista = self.server.get_entries(n_letters)
            if len(lista) < 1:
                raise ValueError
            cena = 0
            for i in range(len(lista)):
                cena += lista[i].price
            return cena
        except(ValueError, listTooLong):
            return None
#MOJE SPRAWDZENIE!
klient = Client(serw)
print(klient.get_total_price(6))