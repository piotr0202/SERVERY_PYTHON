"""
@stworzenie wlasnego wyjatku
dla listy przekraczajacej max liczbe elementow
zdefiniowana jako atrybut klasowy klasy Serwer
Server.n_max_returned_entries
"""
class listTooLong(Exception):
    def __init__(self,value):
        self.value = value