class Library:

    def __init__(self):
        self.title = []
        self.autor = []
        self.publish_y = []
    
    def get_m(self, magazine):
        temp = list(magazine)

    def get_b(self, book):
        self.publish_y.append(book)

    if temp [0:2] in self.publish_y:
        self.autor.append(temp[0:2])
        self.title.append(temp[0])

    else:
        biblioteka.get_b(temp[0:2])
        self.autor.append(temp[0:2])
        self.title.append(temp[0])

    def calculate(self):
        lista = []
        sort = []

    for book in self.publish_y:
        k = self.autor.count(book)
        book = [book[0], book[1], k]
        lista.append(book)
        sort = sorted(lista, key = lambda x: x[0])
 
    for obj in sort:
        obj_1 = (obj[0], obj[1], obj[2])
        print(obj_1)
        
biblioteka = Library()
n = int(input())

for i in range(0,n):
    wejscie = eval(input())
    biblioteka.get_m(wejscie)
    
biblioteka.calculate()